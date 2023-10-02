message = input().upper()
final_message = ''
current_str = ''
for i in range(len(message)):
    repetitions = 0
    if message[i].isdigit():
        if i != len(message) - 1:
            if message[i + 1].isdigit():
                repetitions = message[i] + message[i+1]
            else:
                repetitions = message[i]
        else:
            repetitions = message[i]
        final_message += current_str * int(repetitions)
        current_str = ''
    else:
        current_str += message[i]

unique_chars = list(set(final_message))
print(f"Unique symbols used: {len(unique_chars)}")
print(final_message)
