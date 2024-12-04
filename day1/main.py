from collections import Counter

list_left=[]
list_right=[]
filename = "input.txt"
with open(filename, "r") as file:
    for line in file:
        left, right = map(int, line.split())
        list_left.append(left)
        list_right.append(right)



sorted_left = sorted(list_left)
sorted_right = sorted(list_right)

distances = [abs(a - b) for a, b in zip(sorted_left, sorted_right)]
total_distance = sum(distances)

print("Left list sorted", sorted_left)
print("Right list sorted", sorted_right)

print("Total distance", total_distance)

right_count = Counter(list_right)
similarity_score = 0
for num in list_left:
    similarity_score += num * right_count.get(num, 0)  # Multiply by frequency in right list (default 0)

print("Similarity Score:", similarity_score)