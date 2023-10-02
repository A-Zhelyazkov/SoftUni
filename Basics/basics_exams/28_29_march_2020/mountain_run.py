record = float(input())
distance = float(input())
seconds_per_meter = float(input())

gross_time = distance * seconds_per_meter
slowing_down = distance // 50
slowing_down_time = slowing_down * 30
total_time = slowing_down_time + gross_time

if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    difference = total_time - record
    print(f"No! He was {difference:.2f} seconds slower.")