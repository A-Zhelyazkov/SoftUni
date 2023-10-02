string1 = input().split(", ")
string2 = input().split(", ")
final = []
for i in string1:
    for k in string2:
        if i in k:
            final.append(i)
            break

print(final)
