a = int(input())
b = 0
if a <= 100:
    b = 5
elif a <= 1000:
    b = a * 0.2
else:
    b = a * 0.1

if a % 2 == 0:
    b = b + 1
if a % 10 == 5:
    b = b + 2

total_bonus = a + b

print(b)
print(total_bonus)