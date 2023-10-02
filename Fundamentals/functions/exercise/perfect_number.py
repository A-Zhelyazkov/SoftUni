initial_number = int(input())


def perfect_number(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) / 2 == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number(initial_number))