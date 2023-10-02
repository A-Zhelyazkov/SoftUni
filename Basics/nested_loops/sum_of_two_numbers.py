beginning_interval = int(input())
end_interval = int(input())
n = int(input())
counter = 0
flag = False
for i in range(beginning_interval, end_interval + 1):
    for k in range(beginning_interval, end_interval + 1):
        counter += 1
        if i + k == n:
            print(f"Combination N:{counter} ({i} + {k} = {n})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{counter} combinations - neither equals {n}")