import os

symbols = ("-", ",", ".", "!", "?")
curr_dir = os.path.dirname(os.path.abspath(__file__))
text_file = os.path.join(curr_dir, "text1.txt")

with open(text_file, 'r') as file:
    lines = file.readlines()

for line in range(0, len(lines)):
    if line % 2 == 0:
        for char in symbols:
            lines[line] = lines[line].replace(char, "@")

        print(*lines[line].split()[::-1])

