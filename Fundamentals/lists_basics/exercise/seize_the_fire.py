cell_input = input().split("#")
water = int(input())
total_fire = 0
processed_cells = []
for i in cell_input:
    cell_info = i.split(" = ")
    cell = cell_info[0]
    amount = int(cell_info[1])

    if cell == "High":
        if (81 > amount or amount > 125) or amount > water:
            continue
        else:
            water -= amount
            total_fire += amount

    if cell == "Medium":
        if (51 > amount or amount > 80) or amount > water:
            continue
        else:
            water -= amount
            total_fire += amount

    if cell == "Low":
        if (1 > amount or amount > 50) or amount > water:
            continue
        else:
            water -= amount
            total_fire += amount
    processed_cells.append(amount)

total_effort = total_fire * 0.25

print("Cells:")
for i in processed_cells:
    print(f" - {i}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")


