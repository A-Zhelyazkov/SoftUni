text = input()

while True:
    line = input()
    if line == "End":
        break
    line = line.split()
    command = line[0]

    if command == "Translate":
        char = line[1]
        replacement = line[2]
        text = text.replace(char, replacement)
        print(text)
    elif command == "Includes":
        substring = line[1]
        if substring in text:
            print("True")
        else:
            print("False")
    elif command == "Start":
        substring = line[1]
        if text.startswith(substring):
            print("True")
        else:
            print("False")
    elif command == "Lowercase":
        text = text.lower()
        print(text)
    elif command == "FindIndex":
        char = line[1]
        for idx in range(len(text) - 1, 0, -1):
            if text[idx] == char:
                print(idx)
                break
    elif command == "Remove":
        start_index = int(line[1])
        count = int(line[2])
        end_index = start_index + count
        text = text[:start_index] + text[end_index:]
        print(text)