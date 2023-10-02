n = int(input())

unique_elements = set()

for i in range(n):
    elements = input().split()

    for element in elements:
        unique_elements.add(element)

for i in unique_elements:
    print(i)