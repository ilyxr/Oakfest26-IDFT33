SQL_ERRORS = [
    "sql syntax",
    "mysql",
    "sqlite",
    "postgres",
    "unterminated",
    "odbc",
    "database error",
    "query failed"
]

def detect_issues(test_results):
    issues = []
    for result in test_results:
        if "response" in result:
            text = result["response"].lower()
            #daisy daisy give me your answer do
            #does this look like a SQL error to you?
            #if it does, im a lolicon too
            #damn is 
            #ENRIQUEEE

            for err in SQL_ERRORS:
                if err in text:
                    issues.append({
                        "param": result["param"],
                        "payload": result["payload"],
                        "issue": "Possible SQL injection",
                        "indicator": err
                    })

    return issues
