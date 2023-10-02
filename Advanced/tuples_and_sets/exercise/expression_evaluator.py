from collections import deque
string_expr = deque(input().split())

for ch in range(len(string_expr)):
    current_nums = []

    if string_expr[ch].isdigit():
        current_nums.append(string_expr[ch])
    else:
        if string_expr[ch] == "+":
            result = sum(current_nums)
            string_expr[:ch+1] = result

        elif string_expr[ch] == "-":
            result = sum(current_nums)
            for i in current_nums:
                result -= i
            string_expr[:ch + 1] = result

        elif string_expr[ch] == "*":
            result = 1
            for i in current_nums:
                result *= i
            string_expr[:ch + 1] = result

        elif string_expr[ch] == "/":
            pass