import re

file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please ensure the file path is correct.")
    data = ""

print(data)


def check_for_valid_output(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"  # Regex for valid mul instructions
    matches = re.findall(pattern, data)
    return matches

def calculate_sum(matches):
    total_sum = sum(int(x) * int(y) for x, y in matches)
    return total_sum

matches = check_for_valid_output(data)
result = calculate_sum(matches)

print("The sum of all valid multiplications is:", result)