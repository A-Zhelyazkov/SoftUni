n = int(input())

even_sum = set()
odd_sum = set()
line = 0
for _ in range(n):
    name = input()
    line += 1
    ascii_value = 0

    for i in name:
        ascii_value += ord(i)

    ascii_value //= line
    if ascii_value % 2 == 0:
        even_sum.add(ascii_value)
    else:
        odd_sum.add(ascii_value)

if sum(even_sum) == sum(odd_sum):
    result = odd_sum.union(even_sum, ", ")
    print(', '.join(str(i) for i in result))
elif sum(even_sum) < sum(odd_sum):
    result = odd_sum.difference(even_sum, ", ")
    print(', '.join(str(i) for i in result))
else:
    result = odd_sum.symmetric_difference(even_sum)
    print(', '.join(str(i) for i in result))