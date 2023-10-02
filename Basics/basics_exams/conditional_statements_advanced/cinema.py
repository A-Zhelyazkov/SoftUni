projection = input()
rows = int(input())
columns = int(input())
price = 0

room_size = rows * columns

if projection == "Premiere":
    price = room_size * 12
elif projection == "Normal":
    price = room_size * 7.5
elif projection == "Discount":
    price = room_size * 5

print(f"{price:.2f} leva")
