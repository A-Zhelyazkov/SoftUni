n = int(input())

longest_intersection = []

for _ in range(n):
    data = input().split("-")

    first_range = data[0]
    second_range = data[1]

    a, b = first_range.split(",")
    c, d = second_range.split(",")

    intersection1 = set([int(i) for i in range(int(a), int(b) + 1)])
    intersection2 = set([int(i) for i in range(int(c), int(d)+1)])

    current_intersection = intersection1.intersection(intersection2)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

longest_intersection = list(longest_intersection)

print(f"Longest intersection is [{', '.join(str(i) for i in longest_intersection)}] with length {len(longest_intersection)}")

