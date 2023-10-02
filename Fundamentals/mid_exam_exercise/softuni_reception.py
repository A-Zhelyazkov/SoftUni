efficiency1 = int(input())
efficiency2 = int(input())
efficiency3 = int(input())
students_count = int(input())
count_hours = 0

total_students_per_hour = efficiency1 + efficiency2 + efficiency3

while students_count > 0:
    count_hours += 1
    if count_hours % 4 == 0:
        continue
    if students_count >= total_students_per_hour:
        students_count -= total_students_per_hour
    else:
        students_count = 0

print(f"Time needed: {count_hours}h.")