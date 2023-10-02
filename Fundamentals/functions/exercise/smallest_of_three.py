number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def smallest_of_three(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    elif n3 < n1 and n3 < n2:
        return n3


result = smallest_of_three(number_1, number_2, number_3)
print(result)