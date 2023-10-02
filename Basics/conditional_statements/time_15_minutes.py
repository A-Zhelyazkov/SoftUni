hours = int(input())
minutes = int(input())

total_minutes = (hours * 60) + minutes + 15

total_hours = total_minutes // 60

if total_hours > 23:
    total_hours = total_hours - 24

minutes_sol = total_minutes % 60

if minutes_sol < 10:
    print(f"{total_hours}:0{minutes_sol}")
else:
    print(f"{total_hours}:{minutes_sol}")