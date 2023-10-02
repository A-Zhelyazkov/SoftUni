wanted_book = input()

searched_book = input()
counter = 0
flag = False
while searched_book != "No More Books":
    if searched_book == wanted_book:
        flag = True
        break
    counter += 1
    searched_book = input()

if flag:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")


