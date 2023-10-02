n = int(input())
counter = 0
flag = False
if n == 1:
    print("False")
    exit()
for i in range(2, n):
    if n % i == 0:
        flag = True
        break


if flag:
    print("False")
else:
    print("True")