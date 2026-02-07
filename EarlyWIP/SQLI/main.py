# main.py
#like and sub
from crawler import find_inputs
from tester import test_endpoint # type: ignore
from detector import detect_issues
from report import generate_report # type: ignore

TARGET = input("enter localhost url")

def run():
    print("checking the following: :", TARGET)
    endpoints = find_inputs(TARGET)
    all_results = []
    for ep in endpoints:
        print("Testing endpoint:", ep["url"])
        results = test_endpoint(ep)
        all_results.extend(results)
    issues = detect_issues(all_results)
    generate_report(issues)


if __name__ == "__main__":
    run()
