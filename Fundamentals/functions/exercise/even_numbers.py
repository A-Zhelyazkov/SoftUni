input_ints = [int(i) for i in input().split()]


def evens(x):
    if x % 2 == 0:
        return True
    else:
        return False


even_nums_iterator = filter(evens, input_ints)

even_nums_list = list(even_nums_iterator)
print(even_nums_list)