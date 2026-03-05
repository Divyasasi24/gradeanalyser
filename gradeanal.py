def process_scores(students):
    averages = {}
    for name in students:
        scores = students[name]
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages

def classify_grades(averages):
    result = {}
    for name in averages:
        avg = averages[name]

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "F"

        result[name] = (avg, grade)
    return result

def generate_report(classified, passing_avg=70):

    passed = 0
    total = len(classified)
    print("Student Report")

    for name in classified:
        avg, grade = classified[name]

        if avg >= passing_avg:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"

        print(name, "| Avg:", avg, "| Grade:", grade, "| Status:", status)

    failed = total - passed

    print("Total Students:", total)
    print("Passed:", passed)
    print("Failed:", failed)
    return passed

def main():

    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62],
        "Clara": [95, 98, 96]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)

main()