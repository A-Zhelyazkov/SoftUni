char_1 = input()
char_2 = input()


def ascii_range(a, b):
    for i in range(ord(a)+1, ord(b)):
        print(chr(i), end=" ")
    print()


ascii_range(char_1, char_2)