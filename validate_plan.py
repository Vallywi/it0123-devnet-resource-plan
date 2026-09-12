import json
import sys
from pathlib import Path


PLAN_PATH = Path("student_plan.json")
USE_CASES_PATH = Path("devnet_use_cases.json")
VALID_RESOURCES = {
    "learning-lab",
    "always-on-sandbox",
    "reservation-sandbox",
    "code-exchange",
}
VALID_STATUSES = {"verified", "partially-verified", "rejected"}
EXPECTED_BY_USE_CASE = {
    "UC-01": "learning-lab",
    "UC-02": "always-on-sandbox",
    "UC-03": "reservation-sandbox",
    "UC-04": "code-exchange",
}


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Missing required file: {path}")
        sys.exit(1)
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON in {path}: {exc}")
        sys.exit(1)


def non_empty(value):
    return isinstance(value, str) and bool(value.strip())


def check(name, condition, errors):
    if condition:
        print(f"PASS: {name}")
        return 1
    print(f"FAIL: {name}")
    errors.append(name)
    return 0


def main():
    plan = load_json(PLAN_PATH)
    use_cases = load_json(USE_CASES_PATH)
    decisions = plan.get("decisions", [])
    errors = []
    score = 0

    use_case_ids = {item.get("id") for item in use_cases}
    decision_ids = [item.get("use_case_id") for item in decisions]

    score += check("1/9 plan contains four decisions", len(decisions) == 4, errors)
    score += check("2/9 all required use cases are represented", set(decision_ids) == use_case_ids == set(EXPECTED_BY_USE_CASE), errors)
    score += check("3/9 resource labels are valid", all(item.get("recommended_resource") in VALID_RESOURCES for item in decisions), errors)
    score += check("4/9 resource choices match scenario requirements", all(item.get("recommended_resource") == EXPECTED_BY_USE_CASE.get(item.get("use_case_id")) for item in decisions), errors)
    score += check("5/9 verification statuses are valid", all(item.get("verification_status") in VALID_STATUSES for item in decisions), errors)
    score += check("6/9 official evidence uses developer.cisco.com", all(str(item.get("official_source_url", "")).startswith("https://developer.cisco.com/") for item in decisions), errors)
    score += check("7/9 AI recommendation summaries are recorded", all(non_empty(item.get("ai_recommendation_summary")) for item in decisions), errors)
    score += check("8/9 official evidence summaries are recorded", all(non_empty(item.get("official_evidence_summary")) for item in decisions), errors)
    score += check("9/9 final decision reasons are recorded", all(non_empty(item.get("final_decision_reason")) for item in decisions), errors)

    print(f"\nResult: {score}/9 checks passed")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
