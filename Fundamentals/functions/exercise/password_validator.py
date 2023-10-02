password_input = input()


def is_pass_valid(password):
    is_valid = True

    if 6 > len(password) or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    else:
        pass

    if password.isalnum():
        pass
    else:
        print("Password must consist only of letters and digits")
        is_valid = False

    check_numbers = sum(1 for x in password if x.isdigit())
    if check_numbers < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    else:
        pass

    if is_valid:
        print("Password is valid")


is_pass_valid(password_input)
