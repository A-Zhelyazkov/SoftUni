numbers = [int(i) for i in input().split()]
target = int(input())

for i in range(len(numbers)):
    for k in range(i+1, len(numbers)):
        if numbers[i] + numbers[k] == target:
            print(f"{numbers[i]} + {numbers[k]} = {target}")