input_ints = [int(i) for i in input().split(", ")]


def palindrome_integers(n):
    for num in input_ints:
        num_as_str = str(num)
        for i in num_as_str:
            if int(num_as_str[0]) == int(num_as_str[-1]):
                print("True")
                break
            else:
                print("False")
                break


palindrome_integers(input_ints)
