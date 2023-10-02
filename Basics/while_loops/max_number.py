import sys

max_number = -sys.maxsize
user_input = input()

while user_input != "Stop":
    n = int(user_input)
    if n > max_number:
        max_number = n
    user_input = input()

print(max_number)