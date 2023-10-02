def data_type(command, number):
    result = 0
    if command == "int":
        int_num = float(number)
        result = int_num * 2
        return f"{result:.0f}"
    elif command == "real":
        int_num = float(number)
        result = int_num * 1.5
        return f"{result:.2f}"
    elif command == "string":
        return f"${number}$"


initial_input = input()
value = input()
print(data_type(initial_input, value))
