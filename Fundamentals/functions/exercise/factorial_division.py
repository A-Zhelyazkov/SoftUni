factorial_num = int(input())
divisor = int(input())


def factorial_division(factorial_num, divisor):
    result_factorial = 1
    result_divisor = 1
    for i in range(1, factorial_num + 1):
        result_factorial *= i

    for k in range(1, divisor + 1):
        result_divisor *= k

    final_result = result_factorial / result_divisor
    print(f"{final_result:.2f}")


factorial_division(factorial_num, divisor)