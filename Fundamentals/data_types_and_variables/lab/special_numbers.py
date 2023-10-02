n = int(input())
for i in range(1, n + 1):
    sum_of_ch = 0
    for ch in str(i):
        sum_of_ch += int(ch)
    if sum_of_ch == 5 or sum_of_ch == 7 or sum_of_ch == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")



