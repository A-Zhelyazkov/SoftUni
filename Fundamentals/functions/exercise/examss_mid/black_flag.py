days = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())
final_plunder = 0
count_days = 0
while days > count_days:
    count_days += 1
    final_plunder += plunder_per_day

    if count_days % 3 == 0:
        final_plunder += plunder_per_day * 0.5

    if count_days % 5 == 0:
        final_plunder *= 0.7

if final_plunder >= expected_plunder:
    print(f"Ahoy! {final_plunder:.2f} plunder gained.")
else:
    percentage_plunder = (final_plunder / expected_plunder) * 100
    print(f"Collected only {percentage_plunder:.2f}% of the plunder.")
