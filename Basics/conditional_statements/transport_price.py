n = int(input())
period = input()

if n < 20:
    if period == "day":
        total = 0.7 + (n * 0.79)
    if period == "night":
        total = 0.7 + (n * 0.9)

if 20 <= n < 100:
    total = n * 0.09

if n >= 100:
    total = n * 0.06

print(f"{total:.2f}")





