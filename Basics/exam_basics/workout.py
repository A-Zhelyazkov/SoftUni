import math

days = int(input())
km = float(input())
total_km = km
previous_day = km

for i in range(days):
    norm = int(input()) / 100
    distance_day = previous_day + (previous_day * norm)
    previous_day = distance_day
    total_km += distance_day

diff = math.ceil(abs(total_km - 1000))
if total_km >= 1000:
    print(f"You've done a great job running {diff} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")