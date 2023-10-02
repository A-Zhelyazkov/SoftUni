import sys

min_number = sys.maxsize
user_input = input()

while user_input != "Stop":
    n = int(user_input)
    if n < min_number:
        min_number = n
    user_input = input()

print(min_number)