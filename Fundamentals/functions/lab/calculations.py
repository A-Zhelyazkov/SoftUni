operator_input = input()
first_num = int(input())
second_num = int(input())


def calculator(operator, n1, n2):
    if operator == "multiply":
        return n1 * n2
    elif operator == "divide":
        return n1 // n2
    elif operator == "add":
        return n1 + n2
    elif operator == "subtract":
        return n1 - n2


result = calculator(operator_input, first_num, second_num)
print(result)