n = int(input())

chars = ".,_"
for i in range(n):
    string = input()
    if any(b in chars for b in string):
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
