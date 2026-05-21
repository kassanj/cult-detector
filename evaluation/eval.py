"""
Automated evaluation suite using LangSmith.
Run this to score your chain across test cases.
LangSmith dashboard: https://smith.langchain.com

Run from project root:
    python3 -m evaluation.eval
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from langsmith import Client
from langsmith.evaluation import evaluate
from chain import analyze

client = Client()

# Test dataset — create this in LangSmith or use inline
TEST_CASES = [
    {
        "input": "My book club meets weekly and we discuss one book. The host picks the books.",
        "expected_range": (0, 25),
        "label": "normal_group"
    },
    {
        "input": "Our startup requires all employees to attend a 3-day onboarding retreat where we learn the company values. Phones are collected for the first day to help you focus.",
        "expected_range": (30, 60),
        "label": "mild_concern"
    },
    {
        "input": "The leader communicates through a chosen inner circle. Members who leave are described as spiritually lost. All major life decisions require approval from leadership.",
        "expected_range": (70, 100),
        "label": "high_concern"
    },
]


def score_evaluator(run, example):
    """Check if score falls within expected range."""
    try:
        result = run.outputs
        score = result.get("score", 0)
        expected_min, expected_max = example.outputs["expected_range"]
        in_range = expected_min <= score <= expected_max
        return {
            "key": "score_in_range",
            "score": 1 if in_range else 0,
            "comment": f"Score {score} {'in' if in_range else 'outside'} expected range {expected_min}-{expected_max}"
        }
    except Exception as e:
        return {"key": "score_in_range", "score": 0, "comment": str(e)}


def has_evidence_evaluator(run, example):
    """Check that evidence is cited."""
    try:
        indicators = run.outputs.get("indicators_found", [])
        has_sources = all(i.get("source") for i in indicators)
        return {
            "key": "has_cited_evidence",
            "score": 1 if (len(indicators) > 0 and has_sources) else 0
        }
    except:
        return {"key": "has_cited_evidence", "score": 0}


if __name__ == "__main__":
    print("Running evaluation suite...")
    print("View results at: https://smith.langchain.com\n")

    # Run the chain on each test case and score it
    for case in TEST_CASES:
        print(f"Testing: {case['label']}")
        result = analyze(case["input"])
        score = result.get("score", 0)
        expected_min, expected_max = case["expected_range"]
        passed = expected_min <= score <= expected_max
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status} — Score: {score} (expected {expected_min}-{expected_max})")
        print(f"  Verdict: {result.get('verdict', '')}\n")