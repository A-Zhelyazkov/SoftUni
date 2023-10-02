import sys

count_numbers = int(input())
max_num = -sys.maxsize
total_sum = 0

for _ in range(count_numbers):
    numbers = int(input())
    if numbers > max_num:
        max_num = numbers
    total_sum += numbers

total_small_nums = total_sum - max_num

if max_num == total_small_nums:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - total_small_nums)
    print("No")
    print(f"Diff = {diff}")
