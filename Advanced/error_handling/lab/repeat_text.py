text = input()

try:
    n = int(input())
    print(text * n)
except ValueError:
    print(f"Variable times must be an integer")