usernames = input().split(", ")
valid_names = []
acceptable_symbols = True
for username in usernames:
    if 2 < len(username) < 17:
        pass
    else:
        continue

    for i in username:
        if i.isalnum() or i == "-" or i == "_":
            acceptable_symbols = True
        else:
            acceptable_symbols = False
            break
    if not acceptable_symbols:
        continue

    if " " in username:
        continue

    valid_names.append(username)


for i in valid_names:
    print(i)


