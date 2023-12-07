# def recursive_fib(n):
#     if n <= 1:
#         return 1
#     return recursive_fib(n-1) + recursive_fib(n-2)   ---> not recommended with recursion




def get_fib(n):
    fib1 = 1
    fib2 = 1
    result = 0

    for _ in range(n-1):
        result = fib1 + fib2
        fib1, fib2 = fib2, result

    return result


n = int(input())


print(get_fib(n))