equation = input()
stack_chars = []

for i in range(len(equation)):
    if equation[i] == "(":
        stack_chars.append(i)

    if equation[i] == ")":
        first_parenth = stack_chars.pop()
        last_parenth = i + 1
        print(equation[first_parenth:last_parenth])
