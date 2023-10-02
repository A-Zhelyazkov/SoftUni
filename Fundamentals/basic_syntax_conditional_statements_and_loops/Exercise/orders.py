n = int(input())
total = 0
for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if (price_per_capsule < 0.01 or price_per_capsule > 100) or (days < 1 or days > 31) or (capsules_needed_per_day < 1 or capsules_needed_per_day > 2000):
        continue
    price_day = (days * capsules_needed_per_day) * price_per_capsule
    print(f"The price for the coffee is: ${price_day:.2f}")
    total += price_day

print(f"Total: ${total:.2f}")

