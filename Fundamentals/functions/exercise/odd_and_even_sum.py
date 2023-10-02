number = input()


def odd_and_even_sum(num):
    counter_odd = 0
    counter_even = 0
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            counter_even += int(num[i])
        else:
            counter_odd += int(num[i])

    return f"Odd sum = {counter_odd}, Even sum = {counter_even}"


result = odd_and_even_sum(number)
print(result)
