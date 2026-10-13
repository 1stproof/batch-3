from __future__ import annotations

import json
import os
import signal
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest import mock

SUBMISSION_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SUBMISSION_ROOT))

from src import run


class InputTests(unittest.TestCase):
    def test_parse_input_and_sanitize_unsafe_id(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text(
                json.dumps(
                    {
                        "problems": [
                            {"id": "prob-001", "latex": "First"},
                            {"id": "../odd/id", "latex": "Second"},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            problems = run.parse_input(path)
        self.assertEqual(problems[0].output_name, "prob-001.tex")
        self.assertEqual(problems[1].output_name, "odd-id.tex")

    def test_duplicate_problem_id_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text(
                json.dumps(
                    {
                        "problems": [
                            {"id": "same", "latex": "First"},
                            {"id": "same", "latex": "Second"},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate problem id"):
                run.parse_input(path)

    def test_sanitized_name_collisions_get_distinct_artifact_directories(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text(
                json.dumps(
                    {
                        "problems": [
                            {"id": "a/b", "latex": "First"},
                            {"id": "a?b", "latex": "Second"},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            first, second = run.parse_input(path)
        self.assertNotEqual(first.slug, second.slug)
        self.assertNotEqual(first.output_name, second.output_name)

    def test_hash_suffixed_collision_is_rechecked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text(
                json.dumps(
                    {
                        "problems": [
                            {"id": "a-b-c2a7b64a2d", "latex": "First"},
                            {"id": "a/b", "latex": "Second"},
                            {"id": "a?b", "latex": "Third"},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            problems = run.parse_input(path)
        self.assertEqual(len({problem.slug for problem in problems}), 3)
        self.assertEqual(len({problem.output_name for problem in problems}), 3)


class LifecycleTests(unittest.TestCase):
    def test_terminal_state_is_distinguished_from_active_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            job = Path(directory)
            loop = job / ".humanize" / "rlcr" / "20261001-000000"
            loop.mkdir(parents=True)
            (loop / "state.md").write_text("active", encoding="utf-8")
            self.assertEqual(run.humanize_lifecycle(job), "active")
            (loop / "state.md").rename(loop / "maxiter-state.md")
            self.assertEqual(run.humanize_lifecycle(job), "maxiter")

    def test_outer_hook_timeout_covers_two_reviews(self) -> None:
        self.assertGreater(
            run.HOOK_TIMEOUT_SECONDS,
            2 * run.REVIEW_TIMEOUT_SECONDS,
        )

    @unittest.skipUnless(
        Path("/proc").is_dir() and shutil.which("timeout"),
        "requires Linux procfs and GNU timeout",
    )
    def test_termination_cleans_nested_process_groups(self) -> None:
        parent_code = (
            "import subprocess, sys, time; "
            "subprocess.Popen(['timeout','120',sys.executable,'-c',"
            "'import os,time; print(os.getpid(),os.getpgrp(),flush=True); "
            "time.sleep(120)']); time.sleep(120)"
        )
        process = subprocess.Popen(
            [sys.executable, "-c", parent_code],
            stdout=subprocess.PIPE,
            text=True,
            start_new_session=True,
        )
        assert process.stdout is not None
        _child_pid, child_group = map(int, process.stdout.readline().split())
        self.assertNotEqual(child_group, process.pid)
        run.terminate_process_session(process, grace_seconds=0.2)
        deadline = time.monotonic() + 2
        while run.session_processes(process.pid) and time.monotonic() < deadline:
            time.sleep(0.05)
        self.assertIsNotNone(process.poll())
        self.assertEqual(run.session_processes(process.pid), {})
        process.stdout.close()

    def test_termination_signal_stops_registered_worker_sessions(self) -> None:
        controller = run.ShutdownController()
        process = mock.Mock()
        process.pid = 12345
        self.assertTrue(controller.register(process))

        with mock.patch.object(run, "signal_process_session") as signal_session:
            controller.request(signal.SIGTERM)

        self.assertTrue(controller.event.is_set())
        self.assertEqual(controller.signal_number, signal.SIGTERM)
        signal_session.assert_called_once_with(process.pid, signal.SIGTERM)
        controller.unregister(process)

    def test_external_termination_force_kills_sigterm_resistant_worker(self) -> None:
        stubborn_worker = (
            "import signal,time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
            "print('ready', flush=True); "
            "time.sleep(30)"
        )
        result: list[tuple[int, str | None]] = []
        run.SHUTDOWN.reset()
        try:
            with tempfile.TemporaryDirectory() as directory:
                job = Path(directory)
                event_path = job / "events.jsonl"
                (job / "worker-prompt.md").write_text("prompt", encoding="utf-8")
                with mock.patch.object(
                    run, "codex_command", return_value=[sys.executable, "-c", stubborn_worker]
                ), mock.patch.object(run, "SHUTDOWN_GRACE_SECONDS", 0.1):
                    worker = threading.Thread(
                        target=lambda: result.append(
                            run.run_codex_attempt(
                                job,
                                job / "codex-home",
                                event_path,
                                job / "stderr.log",
                                20,
                            )
                        )
                    )
                    worker.start()
                    deadline = time.monotonic() + 2
                    while not run.SHUTDOWN._processes and time.monotonic() < deadline:
                        time.sleep(0.01)
                    self.assertTrue(run.SHUTDOWN._processes)
                    while time.monotonic() < deadline:
                        if event_path.is_file() and "ready" in event_path.read_text():
                            break
                        time.sleep(0.01)
                    self.assertIn("ready", event_path.read_text())
                    run.SHUTDOWN.request(signal.SIGTERM)
                    worker.join(timeout=3)
                    self.assertFalse(worker.is_alive())
        finally:
            run.SHUTDOWN.reset()

        self.assertEqual(result, [(128 + signal.SIGTERM, "external termination requested")])

    @unittest.skipUnless(Path("/proc").is_dir(), "requires Linux procfs")
    def test_captured_process_timeout_cleans_sigterm_resistant_descendant(self) -> None:
        parent_code = (
            "import signal,subprocess,sys,time; "
            "child=subprocess.Popen([sys.executable,'-c',"
            "'import signal,time; signal.signal(signal.SIGTERM,signal.SIG_IGN); "
            "time.sleep(30)']); "
            "print(child.pid,flush=True); time.sleep(30)"
        )
        run.SHUTDOWN.reset()
        try:
            exit_code, output, stop_reason = run.run_captured_process(
                [sys.executable, "-c", parent_code],
                Path.cwd(),
                timeout_seconds=0.2,
                termination_grace_seconds=0.1,
            )
        finally:
            run.SHUTDOWN.reset()

        child_pid = int(output.strip())
        child_stat = Path(f"/proc/{child_pid}/stat")
        deadline = time.monotonic() + 2
        while child_stat.is_file() and time.monotonic() < deadline:
            fields = child_stat.read_text().rsplit(")", 1)[1].split()
            if fields[0] == "Z":
                break
            time.sleep(0.05)

        self.assertEqual(exit_code, 124)
        self.assertEqual(stop_reason, "timeout")
        if child_stat.is_file():
            self.assertEqual(child_stat.read_text().rsplit(")", 1)[1].split()[0], "Z")


class KimiProviderTests(unittest.TestCase):
    def test_authentication_requires_kimi_key(self) -> None:
        with mock.patch.dict("os.environ", {}, clear=True):
            self.assertFalse(run.authentication_available())
        with mock.patch.dict("os.environ", {"KIMI_API_KEY": "fixture-key"}, clear=True):
            self.assertTrue(run.authentication_available())

    def test_rust_cat_upstream_is_rejected(self) -> None:
        with mock.patch.dict(
            "os.environ",
            {
                "KIMI_UPSTREAM_URL_1": "https://api.rust.cat",
                "KIMI_UPSTREAM_URL_2": "https://node-2.example",
            },
            clear=True,
        ):
            with self.assertRaisesRegex(ValueError, "rust.cat"):
                run.kimi_upstream_urls()

    def test_two_upstreams_and_keys_are_configured_independently(self) -> None:
        environment = {
            "KIMI_API_KEY_1": "node-one-secret",
            "KIMI_API_KEY_2": "node-two-secret",
            "KIMI_UPSTREAM_URLS": "https://node-1.example,https://node-2.example/",
            "KIMI_PROXY_PORT": "19001",
        }
        with tempfile.TemporaryDirectory() as directory, mock.patch.dict(
            "os.environ", environment, clear=True
        ):
            root = Path(directory)
            first, second = run.serving_nodes()
            run.prepare_codex_home(root / "first", Path("/opt/hook"), first)
            run.prepare_codex_home(root / "second", Path("/opt/hook"), second)
            first_config = (root / "first" / "config.toml").read_text()
            second_config = (root / "second" / "config.toml").read_text()

        self.assertEqual(first.upstream_url, "https://node-1.example")
        self.assertEqual(second.upstream_url, "https://node-2.example")
        self.assertEqual((first.proxy_port, second.proxy_port), (19001, 19002))
        self.assertEqual(first.api_key_env, "KIMI_API_KEY_1")
        self.assertEqual(second.api_key_env, "KIMI_API_KEY_2")
        self.assertIn('base_url = "http://127.0.0.1:19001/v1"', first_config)
        self.assertIn('base_url = "http://127.0.0.1:19002/v1"', second_config)
        self.assertIn('env_key = "KIMI_API_KEY_1"', first_config)
        self.assertIn('env_key = "KIMI_API_KEY_2"', second_config)
        self.assertNotIn("node-one-secret", first_config)
        self.assertNotIn("node-two-secret", second_config)

    def test_ten_problems_are_split_five_per_serving_node(self) -> None:
        problems = [
            run.Problem(index, f"p-{index}", "statement", f"p-{index}", f"p-{index}.tex")
            for index in range(10)
        ]
        with mock.patch.dict(
            "os.environ", {"KIMI_API_KEY": "shared-fixture-key"}, clear=True
        ):
            first, second = run.serving_nodes()
        assignments = run.assign_serving_nodes(problems, (first, second))

        self.assertEqual(
            [assignments[problem.problem_id].name for problem in problems[:5]],
            ["node-1"] * 5,
        )
        self.assertEqual(
            [assignments[problem.problem_id].name for problem in problems[5:]],
            ["node-2"] * 5,
        )

    def test_codex_home_uses_kimi_bridge_without_writing_secret(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with mock.patch.dict(
                "os.environ",
                {"KIMI_API_KEY": "must-not-be-written", "KIMI_PROXY_PORT": "19001"},
                clear=True,
            ):
                node = run.serving_nodes()[0]
                run.prepare_codex_home(root, Path("/opt/hook"), node)
            config = (root / "config.toml").read_text(encoding="utf-8")
            catalog = json.loads((root / "kimi-model-catalog.json").read_text())

        self.assertIn('model_provider = "kimi_batch3"', config)
        self.assertIn('base_url = "http://127.0.0.1:19001/v1"', config)
        self.assertIn('env_key = "KIMI_API_KEY"', config)
        self.assertNotIn("must-not-be-written", config)
        self.assertEqual(catalog["models"][0]["slug"], "moonshotai/Kimi-k3")


class SolutionTests(unittest.TestCase):
    def test_incomplete_worker_draft_is_validated_and_submitted(self) -> None:
        draft = (
            "\\documentclass{article}\n\\begin{document}\n"
            "Latest unfinished proof draft.\n\\end{document}\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "output"
            output.mkdir()
            job = root / "job"
            problem = run.Problem(0, "prob-001", "statement", "prob-001", "prob-001.tex")
            state = run.RunState([problem], output)

            def setup_incomplete_job(
                _problem: run.Problem, job_root: Path, _codex_home: Path
            ) -> None:
                loop = job_root / ".humanize" / "rlcr" / "fixture"
                loop.mkdir(parents=True)
                (loop / "state.md").write_text("active\n", encoding="utf-8")
                (job_root / "solution.tex").write_text(draft, encoding="utf-8")

            run.SHUTDOWN.reset()
            try:
                with mock.patch.object(
                    run, "OUTPUT_DIR", output
                ), mock.patch.object(
                    run, "setup_job", side_effect=setup_incomplete_job
                ), mock.patch.object(
                    run, "run_codex_attempt", return_value=(0, None)
                ), mock.patch.object(
                    run, "compile_solution", return_value=(True, 3, None)
                ) as compile_solution:
                    run.solve_problem(
                        problem,
                        {problem.problem_id: job},
                        state,
                        deadline=time.monotonic() + 300,
                        max_restarts=0,
                        codex_home=root / "codex-home",
                    )
            finally:
                run.SHUTDOWN.reset()

            submitted = (output / problem.output_name).read_text(encoding="utf-8")
            status = state.snapshot()[problem.problem_id]

        self.assertEqual(submitted, draft)
        self.assertEqual(status["status"], "incomplete-submitted")
        self.assertFalse(status["humanize_complete"])
        self.assertTrue(status["solution_valid"])
        self.assertEqual(status["solution_pages"], 3)
        self.assertIn("RLCR incomplete", status["incomplete_reason"])
        compile_solution.assert_called_once()

    def test_short_standalone_latex_proof_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "solution.tex"
            path.write_text(
                r"\documentclass{article}\begin{document}By reflexivity, $0=0$.\end{document}",
                encoding="utf-8",
            )
            self.assertLess(path.stat().st_size, 100)
            self.assertTrue(run.valid_solution(path))

    def test_standalone_latex_validation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "solution.tex"
            path.write_text(
                "\\documentclass{article}\n\\begin{document}\n"
                + "A rigorous proof. " * 10
                + "\n\\end{document}\n",
                encoding="utf-8",
            )
            self.assertTrue(run.valid_solution(path))
            path.write_text("not latex", encoding="utf-8")
            self.assertFalse(run.valid_solution(path))

    def test_generated_fallback_escapes_identifier(self) -> None:
        problem = run.Problem(0, "raw", "statement", "with_under", "with_under.tex")
        generated = run.blank_solution(problem, "failure with a 50% sign")
        self.assertIn(r"with\_under", generated)
        self.assertNotIn("50%", generated)
        self.assertTrue(generated.rstrip().endswith(r"\end{document}"))

    def test_compiled_solution_enforces_page_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            solution = root / "solution.tex"
            log = root / "validation.log"
            solution.write_text(
                r"\documentclass{article}\begin{document}Proof.\end{document}",
                encoding="utf-8",
            )
            compile_16 = (
                0,
                (
                    "Output written on /tmp/first-proof-latex-abcdefgh/solution.pdf "
                    "(16 pages, 12345\n6 bytes).\n"
                ),
                None,
            )
            metadata_16 = (
                0,
                "Title: proof\nPages:          16\nPDF version:    1.5\n",
                None,
            )
            compile_17 = (0, "Latexmk: All targets are up-to-date\n", None)
            metadata_17 = (0, "Pages:          17\n", None)
            with mock.patch.object(
                run.shutil, "which", side_effect=lambda command: f"/usr/bin/{command}"
            ), mock.patch.object(
                run,
                "run_captured_process",
                side_effect=[compile_16, metadata_16, compile_17, metadata_17],
            ):
                valid, pages, error = run.compile_solution(solution, log)
                self.assertTrue(valid)
                self.assertEqual(pages, 16)
                self.assertIsNone(error)
                latexmk_command = run.run_captured_process.call_args_list[0].args[0]
                self.assertIn("-norc", latexmk_command)
                self.assertIn("-pdflatex=pdflatex -no-shell-escape %O %S", latexmk_command)
                self.assertEqual(
                    run.run_captured_process.call_args_list[1].args[0][0],
                    "/usr/bin/pdfinfo",
                )

                valid, pages, error = run.compile_solution(solution, log)

        self.assertFalse(valid)
        self.assertEqual(pages, 17)
        self.assertIn("maximum is 16", error or "")


class EndToEndHarnessTests(unittest.TestCase):
    def test_main_converts_one_problem_into_complete_submission_artifacts(self) -> None:
        fake_worker_source = r'''
import json
import os
import subprocess
from pathlib import Path

job = Path.cwd()
loop = job / ".humanize" / "rlcr" / "fixture"
(job / "solution.tex").write_text(
    "\\documentclass{article}\n\\begin{document}\nProof.\n\\end{document}\n",
    encoding="utf-8",
)
(loop / "state.md").unlink()
(loop / "complete-state.md").write_text("complete\n", encoding="utf-8")
subprocess.run(["git", "add", "solution.tex"], check=True)
subprocess.run(["git", "commit", "-m", "Complete proof"], check=True, stdout=subprocess.DEVNULL)

session_dir = Path(os.environ["CODEX_HOME"]) / "sessions" / "2026" / "10" / "01"
session_dir.mkdir(parents=True, exist_ok=True)
records = [
    {
        "timestamp": "2026-10-01T00:00:00Z",
        "type": "session_meta",
        "payload": {"cwd": str(job.resolve()), "originator": "codex_exec", "source": "exec"},
    },
    {
        "timestamp": "2026-10-01T00:00:01Z",
        "type": "token_usage_record",
        "payload": {
            "thread_id": "thread",
            "turn_id": "turn",
            "session_id": "session",
            "response_id": "response",
            "usage": {
                "input_tokens": 100,
                "cached_input_tokens": 20,
                "cache_write_input_tokens": 0,
                "output_tokens": 30,
                "reasoning_output_tokens": 25,
                "total_tokens": 130,
            },
        },
    },
]
(session_dir / "rollout-fixture.jsonl").write_text(
    "".join(json.dumps(record) + "\n" for record in records), encoding="utf-8"
)
'''
        setup_source = """#!/bin/sh
set -eu
mkdir -p .humanize/rlcr/fixture
printf 'active\\n' > .humanize/rlcr/fixture/state.md
"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_path = root / "input.json"
            output_dir = root / "output"
            work_dir = root / "work"
            humanize_root = root / "humanize"
            setup = humanize_root / "scripts" / "setup-rlcr-loop.sh"
            hook = humanize_root / "hooks" / "loop-codex-stop-hook.sh"
            setup.parent.mkdir(parents=True)
            hook.parent.mkdir(parents=True)
            setup.write_text(setup_source, encoding="utf-8")
            setup.chmod(0o755)
            hook.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
            hook.chmod(0o755)
            fake_worker = root / "fake_worker.py"
            fake_worker.write_text(fake_worker_source, encoding="utf-8")
            input_path.write_text(
                json.dumps(
                    {
                        "problems": [
                            {"id": "smoke-001", "latex": "Prove that $1+1=2$."}
                        ]
                    }
                ),
                encoding="utf-8",
            )

            with mock.patch.multiple(
                run,
                INPUT_PATH=input_path,
                OUTPUT_DIR=output_dir,
                WORK_DIR=work_dir,
                HUMANIZE_ROOT=humanize_root,
                HEARTBEAT_SECONDS=0.01,
            ), mock.patch.dict(
                "os.environ",
                {
                    "KIMI_API_KEY": "fixture-key",
                    "PATH": os.environ["PATH"],
                    "MAX_PARALLEL_PROBLEMS": "1",
                    "MAX_TRANSPORT_RESTARTS": "0",
                    "HARNESS_RUN_SECONDS": "300",
                },
                clear=True,
            ), mock.patch.object(
                run, "codex_command", return_value=[sys.executable, str(fake_worker)]
            ), mock.patch.object(
                run, "start_kimi_proxy", return_value=mock.Mock()
            ) as start_proxy, mock.patch.object(
                run, "stop_kimi_proxy"
            ), mock.patch.object(
                run, "compile_solution", return_value=(True, 1, None)
            ), mock.patch.object(
                run.shutil, "which", side_effect=lambda command: f"/usr/bin/{command}"
            ), mock.patch.object(
                run.signal, "signal"
            ):
                exit_code = run.main()

            manifest = json.loads((output_dir / "run_manifest.json").read_text())
            usage = json.loads((output_dir / "token_usage.json").read_text())

            self.assertEqual(exit_code, 0)
            self.assertTrue((output_dir / "smoke-001.tex").is_file())
            self.assertEqual(manifest["problems"][0]["status"], "complete")
            self.assertEqual(manifest["problems"][0]["serving_node"], "node-1")
            self.assertEqual(manifest["problems"][0]["solution_pages"], 1)
            self.assertEqual(usage["totals"]["input_tokens"], 100)
            self.assertEqual(usage["totals"]["reasoning_output_tokens"], 25)
            self.assertEqual(start_proxy.call_count, 2)
            self.assertTrue(
                (
                    output_dir
                    / "humanize"
                    / "smoke-001"
                    / "fixture"
                    / "complete-state.md"
                ).is_file()
            )


class TokenUsageTests(unittest.TestCase):
    def test_combines_token_records_from_both_node_homes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            problems = [
                run.Problem(index, f"p-{index}", "statement", f"p-{index}", f"p-{index}.tex")
                for index in range(2)
            ]
            jobs = {
                problem.problem_id: root / f"job-{problem.index}" for problem in problems
            }
            homes: list[Path] = []
            for problem, tokens in zip(problems, (11, 22), strict=True):
                home = root / f"codex-home-{problem.index}"
                sessions = home / "sessions"
                sessions.mkdir(parents=True)
                records = [
                    {
                        "timestamp": f"2026-10-01T00:00:0{problem.index}Z",
                        "type": "session_meta",
                        "payload": {"cwd": str(jobs[problem.problem_id].resolve())},
                    },
                    {
                        "timestamp": f"2026-10-01T00:00:1{problem.index}Z",
                        "type": "token_usage_record",
                        "payload": {
                            "response_id": f"response-{problem.index}",
                            "usage": {"input_tokens": tokens, "total_tokens": tokens},
                        },
                    },
                ]
                (sessions / f"rollout-{problem.index}.jsonl").write_text(
                    "".join(json.dumps(record) + "\n" for record in records),
                    encoding="utf-8",
                )
                homes.append(home)

            usage = run.collect_token_usage(problems, jobs, homes, generated_at="fixed")

        self.assertEqual(len(usage["steps"]), 2)
        self.assertEqual(usage["totals"]["input_tokens"], 33)
        self.assertEqual(set(usage["per_problem"]), {"p-0", "p-1"})

    def test_collects_incremental_reasoning_usage_without_double_counting(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            job = root / "job"
            codex_home = root / "shared-codex-home"
            sessions = codex_home / "sessions" / "2026" / "10" / "01"
            sessions.mkdir(parents=True)
            rollout = sessions / "rollout-test.jsonl"
            records = [
                {
                    "timestamp": "2026-10-01T00:00:00Z",
                    "type": "session_meta",
                    "payload": {
                        "cwd": str(job.resolve()),
                        "originator": "codex_exec",
                        "source": {"subagent": "review"},
                    },
                },
                {
                    "timestamp": "2026-10-01T00:00:01Z",
                    "type": "token_usage_record",
                    "payload": {
                        "thread_id": "thread",
                        "turn_id": "turn",
                        "session_id": "session",
                        "response_id": "response",
                        "usage": {
                            "input_tokens": 100,
                            "cached_input_tokens": 20,
                            "output_tokens": 30,
                            "reasoning_output_tokens": 25,
                            "total_tokens": 130,
                        },
                    },
                },
                {
                    "timestamp": "2026-10-01T00:00:02Z",
                    "type": "event_msg",
                    "payload": {"type": "token_count"},
                },
            ]
            rollout.write_text(
                "\n".join(json.dumps(record) for record in records) + "\n",
                encoding="utf-8",
            )
            problem = run.Problem(0, "prob-001", "statement", "prob-001", "prob-001.tex")
            usage = run.collect_token_usage(
                [problem],
                {problem.problem_id: job},
                codex_home,
                generated_at="fixed",
            )

        self.assertEqual(len(usage["steps"]), 1)
        self.assertEqual(usage["steps"][0]["stage"], "review")
        self.assertEqual(usage["totals"]["input_tokens"], 100)
        self.assertEqual(usage["totals"]["output_tokens"], 30)
        self.assertEqual(usage["totals"]["reasoning_output_tokens"], 25)
        self.assertEqual(usage["totals"]["total_tokens"], 130)


if __name__ == "__main__":
    unittest.main()
