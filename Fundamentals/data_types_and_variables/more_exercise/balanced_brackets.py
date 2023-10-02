n = int(input())
flag = False

for i in range(n):
    char = input()

    if char == ")" and flag == False:
        flag = True
        break

    if flag:
        if char == ")":
            flag = False
    if char == "(":
        flag = True

if flag:
    print("UNBALANCED")
else:
    print("BALANCED")

    # 1/10 not working