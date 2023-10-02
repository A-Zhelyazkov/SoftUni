def type_check(curr_type):
    def decorator(func):
        def wrapper(arg):
            if type(arg) == curr_type:
                return func(arg)
            return "Bad Type"

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
