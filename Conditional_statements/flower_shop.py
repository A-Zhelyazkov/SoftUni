from math import floor
from math import ceil

magnolia = int(input())
zumbul = int(input())
rose = int(input())
cactus = int(input())
gift_price = float(input())

total_magnolia = magnolia * 3.25
total_zumbul = zumbul * 4
total_rose = rose * 3.5
total_cactus = cactus * 8
gross_earnings = total_cactus + total_rose + total_zumbul + total_magnolia
taxed_earning = gross_earnings * 0.95

diff = abs(taxed_earning - gift_price)
if taxed_earning >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")