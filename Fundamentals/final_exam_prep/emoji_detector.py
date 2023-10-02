import re

text = input()

pattern_emojis = r'([:*]{2})([A-Z][a-z]{2,})\1'
pattern_nums = r'\d'

matched_emojis = re.finditer(pattern_emojis, text)
matched_emojis_len = re.findall(pattern_emojis, text)
cool_threshold_nums = re.findall(pattern_nums, text)
cool_threshold = 1
for i in cool_threshold_nums:
    cool_threshold *= int(i)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matched_emojis_len)} emojis found in the text. The cool ones are:")
for word in matched_emojis:
    groups = word.groups()
    emoji = groups[1]
    ascii_num = 0
    for char in emoji:
        ascii_num += ord(char)

    if ascii_num >= cool_threshold:
        print(groups[0]+groups[1]+groups[0])