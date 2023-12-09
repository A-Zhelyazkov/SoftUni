def find_ways_to_form_string(strings, target, current_solution=[]):
    if target == '':
        # If the target string is empty, we found a valid solution
        print(' '.join(current_solution))
        return

    for string in strings:
        # Check if the current string is a valid prefix for the target
        if target.startswith(string):
            # Recursively explore with the remaining part of the target
            find_ways_to_form_string(strings, target[len(string):], current_solution + [string])

# Input
input_strings = input().split(", ")
target_string = input().strip()

# Output
find_ways_to_form_string(input_strings, target_string)