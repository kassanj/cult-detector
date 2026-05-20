"""
Quick CLI tool for testing without spinning up the server.
Usage: python3 main.py
"""

from chain import analyze
import json

def main():
    print("\n" + "="*60)
    print("  🔍 IS THIS A CULT? — Cult Likelihood Analyzer")
    print("="*60)
    print("Describe any group, company, or social dynamic.")
    print("Type 'quit' to exit.\n")

    while True:
        description = input("📋 Describe the group: ").strip()

        if description.lower() in ['quit', 'exit', 'q']:
            print("\nStay vigilant. 🕵️")
            break

        if len(description) < 10:
            print("Please provide more detail.\n")
            continue

        print("\n🔄 Analyzing...\n")

        try:
            result = analyze(description)

            score = result['score']
            bar = "█" * (score // 5) + "░" * (20 - score // 5)

            print(f"CULT SCORE:  [{bar}] {score}/100")
            print(f"VERDICT:     {result['verdict']}")
            print(f"RESEMBLES:   {result['closest_cult_match']}")
            print(f"SAFE TO LEAVE: {'Yes' if result['safe_to_leave'] else 'Proceed carefully'}")
            print(f"\nADVICE: {result['advice']}")
            print(f"\nINDICATORS FOUND ({len(result['indicators_found'])}):")

            for i, indicator in enumerate(result['indicators_found'], 1):
                severity_emoji = {"low": "🟡", "medium": "🟠", "high": "🔴"}.get(indicator['severity'], "⚪")
                print(f"  {i}. {severity_emoji} {indicator['indicator']}")
                print(f"     ↳ {indicator['source']}")

            print("\n" + "-"*60 + "\n")

        except Exception as e:
            print(f"Analysis failed: {e}\n")


if __name__ == "__main__":
    main()