#!/usr/bin/env python3
"""
Test submitter: reads each LaTeX problem from the input file,
sends it to an LLM via OpenRouter, and wraps the response
in a verbatim block so the output always compiles.

Also writes per-problem and total token usage to
/data/output/token_usage.json so the counts are reliably
retrieved with the rest of the output (independent of stdout capture).
"""
import json
import os
import signal
import time
import requests

INPUT_PATH = "/data/input/input.json"
OUTPUT_DIR = "/data/output"

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
MODEL = "openai/gpt-4o-mini"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
TIMEOUT_SECONDS = 60
MAX_RETRIES = 5

SYSTEM_PROMPT = "You are a mathematician. Provide a clear, concise proof for the given problem."


class LLMTimeout(Exception):
    pass


def _timeout_handler(signum, frame):
    raise LLMTimeout(f"LLM call exceeded {TIMEOUT_SECONDS}s")


def call_llm(problem_latex: str):
    """Send the problem to the LLM and return (content, usage)."""
    old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(TIMEOUT_SECONDS)
    try:
        resp = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": problem_latex},
                ],
            },
        )
        signal.alarm(0)
    except LLMTimeout:
        raise
    finally:
        signal.signal(signal.SIGALRM, old_handler)
    resp.raise_for_status()
    data = resp.json()
    content = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {}) or {}
    if not content:
        raise ValueError("LLM returned empty response")
    return content, usage


def call_llm_with_retries(problem_latex: str):
    """Call the LLM, retrying on rate limits and timeouts."""
    for attempt in range(MAX_RETRIES):
        try:
            return call_llm(problem_latex)
        except (requests.exceptions.HTTPError, LLMTimeout, ValueError) as e:
            if attempt == MAX_RETRIES - 1:
                raise
            wait = 10 * (attempt + 1)
            print(f"    retry {attempt + 1}/{MAX_RETRIES} after {e}, waiting {wait}s...")
            time.sleep(wait)


def write_usage(totals, per_problem):
    """Write token usage to the output dir so it's retrieved with results."""
    usage_summary = {
        "model": MODEL,
        "totals": totals,
        "per_problem": per_problem,
    }
    path = os.path.join(OUTPUT_DIR, "token_usage.json")
    with open(path, "w") as uf:
        json.dump(usage_summary, uf, indent=2)


with open(INPUT_PATH) as infile:
    data = json.load(infile)

os.makedirs(OUTPUT_DIR, exist_ok=True)

totals = {"prompt": 0, "completion": 0, "reasoning": 0, "total": 0}
per_problem = []

for problem in data["problems"]:
    pid = problem["id"]
    latex = problem["latex"]

    print(f"  {pid}: calling LLM...")
    answer, usage = call_llm_with_retries(latex)
    prompt_t = usage.get("prompt_tokens", 0)
    completion_t = usage.get("completion_tokens", 0)
    reasoning_t = (usage.get("completion_tokens_details", {}) or {}).get("reasoning_tokens", 0)
    total_t = usage.get("total_tokens", prompt_t + completion_t)

    totals["prompt"] += prompt_t
    totals["completion"] += completion_t
    totals["reasoning"] += reasoning_t
    totals["total"] += total_t
    per_problem.append({
        "id": pid,
        "prompt": prompt_t,
        "completion": completion_t,
        "reasoning": reasoning_t,
        "total": total_t,
    })

    print(f"  {pid}: got response ({len(answer)} chars) | tokens: "
          f"prompt={prompt_t} completion={completion_t} reasoning={reasoning_t} total={total_t}")

    # Wrap the LLM response in a verbatim block so the .tex always compiles
    proof_block = (
        "\n\\bigskip\n"
        "\\textbf{LLM Response:}\n\n"
        "\\begin{verbatim}\n"
        f"{answer}\n"
        "\\end{verbatim}\n"
    )

    if r"\end{document}" in latex:
        output = latex.replace(r"\end{document}", proof_block + r"\end{document}")
    else:
        output = latex + "\n" + proof_block

    output_path = os.path.join(OUTPUT_DIR, f"{pid}.tex")
    with open(output_path, "w") as outfile:
        outfile.write(output)

    # Write usage after every problem so partial results survive a timeout/crash.
    write_usage(totals, per_problem)

    print(f"  {pid}.tex written")
    time.sleep(10)  # wait 10s between problems

print(f"\nDone. Wrote {len(data['problems'])} files to {OUTPUT_DIR}")
print(f"Total tokens — prompt: {totals['prompt']}, completion: {totals['completion']}, "
      f"reasoning: {totals['reasoning']}, total: {totals['total']}")