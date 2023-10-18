def num_fact(n):
    if n == 1:
        return 1

    return n * num_fact(n - 1)

num = int(input())

print(num_fact(num))