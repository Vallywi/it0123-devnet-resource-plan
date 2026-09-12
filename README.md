# IT0123 Module 2 DevNet Resource Validation

## Resource Decisions

| Use case | Final resource | Verification | Main reason |
|---|---|---|---|
| UC-01 | `learning-lab` | verified | The scenario needs guided, step-by-step learning before choosing an execution environment. |
| UC-02 | `always-on-sandbox` | verified | The scenario needs immediate shared API exploration without admin access, VPN setup, or configuration changes. |
| UC-03 | `reservation-sandbox` | verified | The scenario needs private isolated configuration testing with administrative control. |
| UC-04 | `code-exchange` | verified | The scenario needs existing sample code or a repository to review and adapt. |

## Official Evidence

- Cisco DevNet lists Labs as automation and programmability labs featuring Cisco platforms: https://developer.cisco.com/learning/
- Cisco DevNet Sandbox documentation distinguishes always-on and reservation-based sandbox access models: https://developer.cisco.com/docs/sandbox/
- Cisco DevNet describes Code Exchange as the place to explore sample solutions and implementations: https://developer.cisco.com/codeexchange/

## Validator Result

`python validate_plan.py` reports `9/9 checks passed`.

## AI Use Disclosure

I used OpenAI Codex / ChatGPT as an AI assistant to draft recommendations, summarize the reasoning, create the local files, and run validation. I treated the AI recommendations as provisional and checked the selected resource categories against official Cisco DevNet pages before accepting them.

## Git Evidence

This folder was initialized as a local Git repository for the activity. The repository contains an initial scaffold commit and a validation milestone commit.
