values = ((float(i) for i in input().split()))
abs_values = []
for num in values:
    abs_values.append(abs(num))

print(abs_values)