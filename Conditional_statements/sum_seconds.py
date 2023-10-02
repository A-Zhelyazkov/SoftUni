a = int(input())
b = int(input())
c = int(input())

total_time = a + b + c

total_minutes = total_time // 60
total_seconds = total_time % 60

if total_seconds < 10:
    print(f"{total_minutes}:0{total_seconds}")
else:
    print(f"{total_minutes}:{total_seconds}")