group_size = int(input())
days = int(input())
days_count = 0
coins = 0
total_companions = group_size
while days > 0:
    days_count += 1
    if days_count % 10 == 0:
        total_companions -= 2
    if days_count % 15 == 0:
        total_companions += 5
    coins += 50
    coins -= 2 * total_companions
    if days_count % 3 == 0:
        coins -= total_companions * 3
    if days_count % 5 == 0:
        coins += total_companions * 20
        if days_count % 3 == 0:
            coins -= total_companions * 2
    days -= 1
coins_per_companion = int(coins / total_companions)
print(f"{total_companions} companions received {coins_per_companion} coins each.")


