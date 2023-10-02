from string import punctuation
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))
text_file = os.path.join(curr_dir, "text.txt1")
output_file = os.path.join(curr_dir, "output.txt")
with open(text_file, 'r') as file:
    lines = file.readlines()


with open(output_file, 'w') as file:
    idx = 0
    for line in lines:
        symbols = 0
        letters = 0
        for char in line:
            if char in punctuation:
                symbols += 1
            elif char.isalpha():
                letters += 1
        file.write(f"Line {idx + 1}: {''.join(lines[idx][:-1])} ({letters})({symbols})\n")
        idx += 1

