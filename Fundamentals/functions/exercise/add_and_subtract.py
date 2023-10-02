def add(a, b):
    return a + b


def subtract(a,b):
    return a - b


def add_and_subtract(a, b, c):
    result_sum = add(a, b)
    result = subtract(result_sum, c)
    return result


a = int(input())
b = int(input())
c = int(input())


print(add_and_subtract(a, b, c))