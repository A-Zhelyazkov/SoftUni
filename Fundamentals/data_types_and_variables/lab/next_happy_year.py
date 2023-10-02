year = int(input())
flag = False
while True:
    if flag:
        break
    year += 1
    string_year = str(year)
    for ch in string_year:
        if string_year.count(ch) == 1:
            flag = True
            continue
        else:
            flag = False
            break
print(year)


