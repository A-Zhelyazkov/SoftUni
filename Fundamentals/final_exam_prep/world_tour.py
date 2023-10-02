def valid_idx(i, txt):
    if 0 <= i < len(txt):
        return True
    return False


stops = input()

while True:
    command = input()

    if command == "Travel":
        break

    command_args = command.split(":")
    action = command_args[0]

    if action == "Add Stop":
        idx = int(command_args[1])
        string = command_args[2]
        if valid_idx(idx, stops):
            stops = stops[:idx] + string + stops[idx:]

    elif action == "Remove Stop":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        if valid_idx(start_idx, stops) and valid_idx(end_idx, stops):
            stops = stops[:start_idx] + stops[end_idx + 1:]

    elif action == "Switch":
        old_str = command_args[1]
        new_str = command_args[2]
        if old_str in stops:
            stops = stops.replace(old_str, new_str)

    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")


