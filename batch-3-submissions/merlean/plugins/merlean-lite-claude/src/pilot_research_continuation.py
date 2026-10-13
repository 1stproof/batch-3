"""Evidence-based main-owned continuation; never mathematical authority."""
import copy

CONTINUATION_MODE = 'main_selected'
CONTINUATION_INSTRUCTION = (
    'Main chooses the next research move from the exact current obstruction, prior work and returned evidence. '
    'Continue or refine the current approach when it still offers useful progress; change it when evidence '
    'shows a representation defect or repeated auxiliary repair leaves the crux untouched. '
    'Advisory options include developing the smallest unresolved inference, comparing an alternative '
    'representation, making a discriminating argument, or reassessing assumptions and independent triage. '
    'These are options, not a rotation or a requirement to change routes. '
    'Explain the chosen move and how it could reduce the obstruction in the existing notes or research_work. '
    'If computation is essential, propose an exact bounded Sol research task for independent approval; '
    'do not claim unexecuted checks. Preserve the original target, useful work, failed approaches and all '
    'unresolved findings.'
)


def validate_research_work(value):
    if value is None:
        return None
    keys = {'objective', 'approach', 'work_performed', 'result', 'next_step', 'failed_approaches'}
    if (not isinstance(value, dict) or set(value) != keys
            or any(not isinstance(value[k], str) or not value[k].strip() for k in keys - {'failed_approaches'})
            or not isinstance(value['failed_approaches'], list)
            or any(not isinstance(v, str) or not v.strip() for v in value['failed_approaches'])):
        raise ValueError('research_work requires substantive objective, approach, work_performed, result, next_step and failed_approaches:string[]')
    return copy.deepcopy(value)
