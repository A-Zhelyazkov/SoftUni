def print_rows(n, count):
    print(" " * (n - count), end='')
    print(*["*"] * count)


n = int(input())

for i in range(n):
    print_rows(n, i)

for i in range(n, 0, -1):
    print_rows(n, i)