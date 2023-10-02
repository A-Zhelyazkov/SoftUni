total_coffee = 0
while True:
    action = input()
    if action == "END":
        break
    if action == "coding" or action == "dog" or action == "cat" or action == "movie":
        total_coffee += 1
    elif action == "CODING" or action == "DOG" or action == "CAT" or action == "MOVIE":
        total_coffee += 2
    else:
        continue

if total_coffee > 5:
    print("You need extra sleep")
else:
    print(total_coffee)

