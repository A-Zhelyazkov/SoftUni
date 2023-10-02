electrons = int(input())
n = 0
final = []
while electrons:
    n += 1
    current_electrons = 2 * (n ** 2)
    final.append(min(electrons, current_electrons))
    electrons -= min(current_electrons, electrons)

print(final)