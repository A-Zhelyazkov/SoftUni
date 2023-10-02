text = input()
explosions = 0
final_str = ''

for i in range(len(text)):
    if explosions > 0 and text[i] != ">":
        explosions -= 1
    elif text[i] == ">":
        final_str += text[i]
        explosions += int(text[i+1])
    else:
        final_str += text[i]

print(final_str)



