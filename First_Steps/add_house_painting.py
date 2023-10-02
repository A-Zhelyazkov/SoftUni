x = float(input())
y = float(input())
h = float(input())

front_door = 1.2 * 2
front_wall = x * x - front_door
back_wall = x * x

window = 1.5 * 1.5
side_wall = x * y - window
side_walls = 2 * side_wall

roof_rectangles = 2 * (x * y)
roof_triangles = 2 * (x * h / 2)

total_green = front_wall + back_wall + side_walls
total_red = roof_triangles + roof_rectangles
litres_green = total_green / 3.4
litres_red = total_red / 4.3

print(f'{litres_green:.2f}')
print(f'{litres_red:.2f}')
