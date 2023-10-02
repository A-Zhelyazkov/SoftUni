def reverse_text(sequennce):
    start = len(sequennce) - 1
    while start > -1:
        yield sequennce[start]
        start -= 1

for char in reverse_text("step"):
    print(char, end='')
