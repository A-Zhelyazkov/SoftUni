lily_age = int(input())
price_washing_machine = float(input())
price_1_toy = int(input())
total_money = 0
total_toys = 0
total_even_bdays = 0

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        total_even_bdays += 1
        total_money += 10 * total_even_bdays
    else:
        total_toys += 1

money_after_steal = total_money - (1 * total_even_bdays)
money_from_toys = total_toys * price_1_toy

total_money_washing_machine = money_from_toys + money_after_steal

diff = abs(total_money_washing_machine - price_washing_machine)
if total_money_washing_machine >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


