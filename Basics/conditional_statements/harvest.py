from math import floor
from math import ceil
x_sq_m_land = int(input())
y_grapes_per_sqm = float(input())
z_needed_l_wine = int(input())
workers = int(input())

total_grapes = x_sq_m_land * y_grapes_per_sqm
grapes_for_wine = total_grapes * 0.4
total_wine = grapes_for_wine / 2.5

grapes_left_for_workers = (total_wine - z_needed_l_wine) / workers
diff = abs(z_needed_l_wine - total_wine)
if total_wine < z_needed_l_wine:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {ceil(total_wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(grapes_left_for_workers)} liters per person.")
