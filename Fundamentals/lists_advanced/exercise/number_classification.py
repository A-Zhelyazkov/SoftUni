sequence = [int(i) for i in input().split(", ")]

positive = [i for i in sequence if i >= 0]
negative = [i for i in sequence if i < 0]
even = [i for i in sequence if i % 2 == 0]
odd = [i for i in sequence if i % 2 != 0]

print(f"Positive: {', '.join(str(i) for i in positive)}")
print(f"Negative: {', '.join(str(i) for i in negative)}")
print(f"Even: {', '.join(str(i) for i in even)}")
print(f"Odd: {', '.join(str(i) for i in odd)}")