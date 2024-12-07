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

    directive_pattern = r"(do\(\)|don't\(\))"
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    enable = True
    valid_instructions = []

    for match in re.finditer(f"{directive_pattern}|{mul_pattern}", data):
        if match.group(1):
            directive = match.group(1)
            print(f"Directive Match: {directive}")
            enable = directive == "do()"
        elif enable and match.group(2) and match.group(3):
            x, y = int(match.group(2)), int(match.group(3))
            print(f"Mul Match: ({x}, {y})")
            valid_instructions.append((x, y))

    return valid_instructions

def calculate_sum(valid_instructions):
    return sum(x * y for x, y in valid_instructions)


matches = check_for_valid_output(data)
result = calculate_sum(matches)

print("The sum of all valid multiplications is:", result)
