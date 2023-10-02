decorations_needed = int(input())
days_until_christmas = int(input())
days_left = days_until_christmas

# prices of decorations
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

# points/shopping
ornament_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17
days_count = 0
total_cost = 0
total_spirit = 0
while days_left != 0:
    days_count += 1
    if days_count % 11 == 0:
        decorations_needed += 2

    if days_count % 2 == 0:
        total_cost += decorations_needed * ornament_set
        total_spirit += ornament_points

    if days_count % 3 == 0:
        total_cost += decorations_needed * (tree_skirt + tree_garland)
        total_spirit += tree_skirt_points + tree_garland_points

    if days_count % 5 == 0:
        total_cost += decorations_needed * tree_lights
        total_spirit += tree_lights_points
        if days_count % 3 == 0:
            total_spirit += 30
    days_left -= 1

    #  cat
    if days_count % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt + tree_garland + tree_lights

if days_until_christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
