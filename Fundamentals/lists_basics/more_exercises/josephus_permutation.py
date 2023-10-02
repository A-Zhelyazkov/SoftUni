people = [int(i) for i in input().split()]
number = int(input())
for i in range(number, len(people), number):
    step = number % len(people)
    people.pop(i)

print(people)
