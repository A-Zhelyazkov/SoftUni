from collections import deque

parentheses = deque(input())

while parentheses:
    if parentheses[0] == "(" and parentheses[-1] == ")":
        parentheses.pop()
        parentheses.popleft()
    if parentheses[0] == "[" and parentheses[-1] == "]":
        parentheses.pop()
        parentheses.popleft()
    if parentheses[0] == "{" and parentheses[-1] == "}":
        parentheses.pop()
        parentheses.popleft()
    else:
        break

if parentheses:
    print("NO")
else:
    print("YES")