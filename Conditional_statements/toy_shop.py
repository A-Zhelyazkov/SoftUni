trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_puzzles = puzzles * 2.6
total_dolls = dolls * 3
total_bears = bears * 4.1
total_minions = minions * 8.2
total_trucks = trucks * 2

total_price = total_puzzles + total_dolls + total_bears + total_minions + total_trucks

count_all = puzzles + dolls + bears + minions + trucks

if count_all >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.9

diff = abs(total_price - trip_price)

if total_price >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")