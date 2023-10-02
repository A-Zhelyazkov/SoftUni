# 1 2 -3 -4 65 -98 12 57 -84

list_nums = [int(i) for i in input().split()]
positives = []
negatives = []

for i in list_nums:
    if i > 0:
        positives.append(i)
    else:
        negatives.append(i)

positive_sum = sum(positives)
negative_sum = sum(negatives)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")