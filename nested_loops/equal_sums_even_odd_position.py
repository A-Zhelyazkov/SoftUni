num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    num_to_str = str(i)
    sum_odd = 0
    sum_even = 0
    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print(i, end=" ")
