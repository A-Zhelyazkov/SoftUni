budget = int(input())

action = input()
while action != "End":
    action = int(action)

    budget -= action
    if budget < 0:
        print("You went in overdraft!")
        exit()
    action = input()

print("You bought everything needed.")






