n = int(input())

for _ in range(n):
    input_line = input().split()
    current_name = ''
    current_age = ''
    for word in input_line:
        if "@" in word and "|" in word:
            start_index = 0
            end_index = 0
            for i in range(len(word)):
                if word[i] == "@" and start_index == 0:
                    start_index = i
                if word[i] == "|" and end_index == 0:
                    end_index = i
            current_name = word[start_index+1:end_index]

        elif "#" in word and "*" in word:
            start_index = 0
            end_index = 0
            for i in range(len(word)):
                if word[i] == "#" and start_index == 0:
                    start_index = i
                if word[i] == "*" and end_index == 0:
                    end_index = i
            current_age = word[start_index+1:end_index]

    print(f"{current_name} is {current_age} years old.")