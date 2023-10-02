command = input()
number = input()


def data_types(command, number):
    result = 0
    if command == "int":
        int_num = int(number)
        result = int_num * 2
        print(result)
    elif command == "real":
        int_num = int(number)
        result = int_num * 1.5
        print(f"{result:.2f}")
    elif command == "string":
        print(f"${number}$")


data_types(command, number)
