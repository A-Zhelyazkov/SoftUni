divisor = int(input())
boundary = int(input())
max_num = 0
for i in range(1, boundary + 1):
    if i % divisor == 0:
        max_num = i

print(max_num)
