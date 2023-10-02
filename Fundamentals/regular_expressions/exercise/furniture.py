import re

furniture = []
total_cost = 0
pattern = r">>([a-zA-z]+)<<(\d+\.?\d+ ?)!(\d+)"
while True:
    command = input()

    if command == "Purchase":
        break

    result = re.findall(pattern, command)
    for i in result:
        furniture.append(i[0])
        total_cost += float(i[1]) * int(i[2])

print(f"Bought furniture:")
for i in furniture:
    print(i)
print(f"Total money spend: {total_cost:.2f}")

