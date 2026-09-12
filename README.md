# IT0123 DevNet Resource Validation Plan

## Student and Project

- Name: Jecyn Vallirie Turbanos
- Section: IT0123
- Repository name: `it0123-devnet-resource-plan`

## Purpose

Selecting the correct Cisco DevNet resource matters because each resource supports a different stage of a network-automation task. A guided lab, shared sandbox, reserved sandbox, or code repository can be useful, but choosing the wrong one can waste time or create unsafe expectations about access, isolation, or administrative privileges.

## Validated Resource Decisions

| Use case | Selected resource | Official evidence | Rationale |
|---|---|---|---|
| UC1 | `always-on-sandbox` | https://developer.cisco.com/docs/sandbox/ | Immediate shared read-only API exploration is needed, and administrative changes are not required. |
| UC2 | `reservation-sandbox` | https://developer.cisco.com/docs/sandbox/ | Private configuration testing needs administrative control, scheduled access, setup time, and possible VPN use. |
| UC3 | `learning-lab` | https://developer.cisco.com/learning/ | The beginner needs guided, step-by-step learning before attempting independent API activity. |
| UC4 | `code-exchange` | https://developer.cisco.com/codeexchange/ | The task starts by reviewing existing automation examples or repositories before designing a solution. |

## AI Evaluation

I accepted the AI recommendation for each use case after checking it against the activity decision guide and official Cisco DevNet pages. The main correction was to align the final answers to the updated starter use-case order: UC1 is `always-on-sandbox`, UC2 is `reservation-sandbox`, UC3 is `learning-lab`, and UC4 is `code-exchange`.

## Validation Evidence

- Validator result: `VALIDATION COMPLETE: 9/9 checks passed.`
- Command used: `python validate_plan.py`
- Official Cisco pages reviewed:
  - https://developer.cisco.com/docs/sandbox/
  - https://developer.cisco.com/learning/
  - https://developer.cisco.com/codeexchange/

## Git Evidence

- Initial commit message: `Initial scaffold for DevNet validation activity`
- Validation commit message: `Complete validated DevNet resource plan`
- Output of `git log --oneline`: recorded from the local repository during submission preparation.

## AI-Use Disclosure

I used OpenAI Codex / ChatGPT as an AI assistant to draft recommendations, summarize the reasoning, compare the starter requirements, update the project files, and run validation. I independently checked the resource labels, official Cisco evidence pages, validator requirements, and final JSON structure before accepting the recommendations.
