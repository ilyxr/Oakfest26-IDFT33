# report generator for the tests idk

def generate_report(issues):
    print("\nreport\n")

    if not issues:
        print("No obvious SQLi indicators detected.")
        return

    for i, issue in enumerate(issues, 1):
        print(f"{i}. Parameter: {issue['param']}")
        print(f"   Payload: {issue['payload']}")
        print(f"   Indicator: {issue['indicator']}")
        print("")

print("Subscribe to LawByMike")