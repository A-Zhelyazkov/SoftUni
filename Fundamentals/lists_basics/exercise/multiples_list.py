factor = int(input())
count = int(input())
multiples = []
current_num = factor
for i in range(count):
    multiples.append(current_num)
    current_num += factor

print(multiples)