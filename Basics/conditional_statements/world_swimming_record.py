world_record = float(input())
distance = float(input())
seconds_per_meter = float(input())

gross_time = distance * seconds_per_meter

resistance = distance // 15

net_time = 12.5 * resistance
total_time = net_time + gross_time
diff = total_time - world_record
if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")