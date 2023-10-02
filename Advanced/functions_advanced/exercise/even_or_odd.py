def even_odd(*args):
    result = []
    command = args[-1]
    nums = [int(i) for i in args[:-1]]
    if command == "even":
        result = [int(i) for i in nums if i % 2 == 0]
    else:
        result = [int(i) for i in nums if i % 2 == 1]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))