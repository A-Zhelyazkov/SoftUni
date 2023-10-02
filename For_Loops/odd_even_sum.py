n = int(input())

sum_even = 0
sum_odd = 0

for count in range(n):
    numbers = int(input())
    if count % 2 == 0:
        sum_even += numbers
    else:
        sum_odd += numbers

if sum_even == sum_odd:
    print("Yes")
    print(f"Sum = {sum_odd}")
else:
    diff = abs(sum_even - sum_odd)
    print("No")
    print(f"Diff = {diff}")