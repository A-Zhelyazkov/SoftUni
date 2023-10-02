import re

data = input()

pattern = r'#[A-Za-z\s]+#[\d]{2}\/[\d]{2}\/[\d]{2}#[\d]+#|\|[A-Z][a-z]+\|[\d]{2}\/[\d]{2}\/[\d]{2}\|[\d]+\|'

filtered_items = re.findall(pattern, data)

total_calories = 0

for item in filtered_items:
    if "|" in item:
        item = item.split("|")
        total_calories += int(item[3])

    elif "#" in item:
        item = item.split("#")
        total_calories += int(item[3])

print(f"You have food to last you for: {total_calories // 2000} days!")

for item in filtered_items:
    if "|" in item:
        item = item.split("|")
        print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")

    elif "#" in item:
        item = item.split("#")
        print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")
