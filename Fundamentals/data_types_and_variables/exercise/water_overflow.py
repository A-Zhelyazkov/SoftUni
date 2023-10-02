n = int(input())
total_liters = 255
total_poured = 0
for i in range(n):
    liters = int(input())
    if liters > total_liters:
        print("Insufficient capacity!")
        continue
    total_poured += liters
    total_liters -= liters

print(total_poured)





