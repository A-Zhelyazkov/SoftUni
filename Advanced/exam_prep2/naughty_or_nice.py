def naughty_or_nice_list(kids, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []

    for data in args:
        number, command = data.split("-")
        number = int(number)
        curr_counter = 0
        iterations = -1
        for num, kid in kids:
            iterations += 1
            if num == number:
                curr_counter += 1

        if curr_counter == 1:
            data = kids.pop(iterations)
            if command == "Naughty":
                naughty.append(data[1])
            elif command == "Nice":
                nice.append(data[1])

    a = 5


print(naughty_or_nice_list(
 [
 (3, "Amy"),
 (1, "Tom"),
 (7, "George"),
 (3, "Katy"),
 ],
 "3-Nice",
 "1-Naughty",
 Amy="Nice",
 Katy="Naughty",
))

