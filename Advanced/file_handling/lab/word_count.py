import os
import re

curr_dir = os.path.dirname(os.path.abspath(__file__))
word_file = "words.txt"
words_dir = os.path.join(curr_dir, word_file)
text_file = "text.txt"
text_dir = os.path.join(curr_dir, text_file)
occurences = {}
with open(words_dir, 'r') as file:
    words = file.read().lower().split()

with open(text_dir, 'r') as file:
    text = file.read().lower()

for special in words:
    print(text.count(special, 0, -1))

# not finished

