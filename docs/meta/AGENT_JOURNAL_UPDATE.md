# Journal Update Playbook for LLM Agent

## Purpose
Single source of truth for automating weekly journal updates when the user says “We need to update the journal.”

## Trigger
- User asks to update the journal (usually for last Mon–Fri).

## Inputs
- Date range (defaults to previous Mon–Fri if not provided).
- Source repos: `/Users/williamgoode/Repositories/ScaylorAI/**`.

## Source Collection (order)
1) Progress reports in `docs/progress_reports/PROGRESS_YYYY-MM-DD.md` across ScaylorAI repos; filter to the target week.
2) If a day is missing, scan recent commits for that repo during the window to recover major accomplishments; otherwise ask the user for that day’s context.

## Summarization Rules
- Voice: Precise, restrained, direct; first-person active; short declarative sentences; no marketing fluff.
- Focus on accomplishments, shipped features, infra changes, key fixes, tests, deployments, and ticket movements.
- Group by week; 6–10 bullets max; prefer impact over detail.

## Edit Steps
1) Open `journal/20250811-current.md`.
2) Append a new week section:
   - Header: `## Week NN (Month DD - Month DD, YYYY)`; increment week number.
   - Bullets: one line each, past-tense achievements aligned with Summarization Rules.
3) Do not edit prior weeks.
4) Preserve markdown style: blank line after header; bullets start with `* `.

## Validation
- Reread the new section for clarity and brevity.
- Ensure dates match the target Mon–Fri window.
- No sensitive data (tokens, PII).

## Handover
- Tell the user the journal was updated and to commit to run the pre-commit hook (which regenerates resume artifacts).

## Safety/Constraints
- Logging: only add notes when relevant; avoid noisy or sensitive details.
- Linear: do not create or modify tickets unless explicitly asked, and only for tickets assigned to Will.
- Testing: none required for markdown edits.

