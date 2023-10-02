sequence = input().split()
result = 0

for equation in sequence:
    current_res = 0
    first_letter = equation[0]
    num = ''
    last_letter = equation[-1]

    for i in range(1, len(equation)):
        if equation[i].isdigit():
            num += equation[i]

    num = int(num)

    if first_letter.isupper():
        position_first = ord(first_letter) - 64
        current_res = num / position_first
    else:
        position_first = ord(first_letter) - 96
        current_res = num * position_first

    if last_letter.isupper():
        position_last = ord(last_letter) - 64
        current_res -= position_last
    else:
        position_last = ord(last_letter) - 96
        current_res += position_last

    result += current_res

print(f"{result:.2f}")








