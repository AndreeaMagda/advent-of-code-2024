file_path = "input.txt"

with open(file_path, "r") as file:
    data = file.read()

reports = [list(map(int, line.split())) for line in data.strip().split("\n")]

def is_safe_report(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    increasing = True
    decreasing = True

    for diff in differences:
        if not (1 <= diff <= 3):
            increasing = False
        if not (-3 <= diff <= -1):
            decreasing = False

    return increasing or decreasing


safe_reports_count = 0
for report in reports:
    if is_safe_report(report):
        safe_reports_count += 1

print(safe_reports_count)
