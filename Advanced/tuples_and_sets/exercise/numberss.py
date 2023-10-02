sequence1 = set(int(i) for i in input().split())
sequence2 = set(int(i) for i in input().split())

for _ in range(int(input())):
    data = input().split()

    command = data[0]
    target = data[1]

    if command == "Add":
        nums_to_add = [int(i) for i in data[2:]]
        if target == "First":
            for i in nums_to_add:
                sequence1.add(i)
        else:
            for i in nums_to_add:
                sequence2.add(i)

    elif command == "Remove":
        nums_to_remove = [int(i) for i in data[2:]]
        if target == "First":
            for i in nums_to_remove:
                if i in sequence1:
                    sequence1.remove(i)
        else:
            for i in nums_to_remove:
                if i in sequence2:
                    sequence2.remove(i)

    elif command == "Check":
        if sequence1.issubset(sequence2) or sequence2.issubset(sequence1):
            print("True")
        else:
            print("False")

sequence1_sorted = sorted(sequence1)
sequence2_sorted = sorted(sequence2)
print(', '.join(str(i) for i in sequence1_sorted))
print(', '.join(str(i) for i in sequence2_sorted))