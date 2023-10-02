string_input = input()
times_to_multiply = int(input())


def repeat_string(initial_string, times):
    return initial_string * times


result = repeat_string(string_input, times_to_multiply)
print(result)