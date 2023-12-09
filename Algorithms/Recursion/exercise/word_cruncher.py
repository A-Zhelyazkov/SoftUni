def find_ways_to_form_string(strings, target, current_solution=[], used=set(), found_combinations=set()):
    if target == '':
        current_combination = tuple(sorted(current_solution))
        if current_combination not in found_combinations:
            found_combinations.add(current_combination)
            print(' '.join(current_solution))
        return

    for i, string in enumerate(strings):
        if i not in used and target.startswith(string):
            # Mark the index as used
            used.add(i)

            remaining_target = target[len(string):]
            find_ways_to_form_string(strings, remaining_target, current_solution + [string], used, found_combinations)

            used.remove(i)


input_strings = input().split(", ")
target_string = input().strip()

find_ways_to_form_string(input_strings, target_string)