count_doubles = int(input())
sum1 = 0
sum2 = 0

for i in range(0, count_doubles * 2):
    numbers = int(input())
    if i < count_doubles:
        sum1 += numbers
    else:
        sum2 += numbers

if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
else:
    diff = abs(sum1 - sum2)
    print(f"No, diff = {diff}")


