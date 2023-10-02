from math import ceil
seq = [int(i) for i in input().split(", ")]
cycles = ceil(max(seq) / 10)
low_boundary = 1
upper_boundary = 10
for i in range(1, cycles+1):
    current_nums = [i for i in seq if low_boundary <= i <= upper_boundary]
    print(f"Group of {upper_boundary}'s: {current_nums}")
    low_boundary += 10
    upper_boundary += 10

