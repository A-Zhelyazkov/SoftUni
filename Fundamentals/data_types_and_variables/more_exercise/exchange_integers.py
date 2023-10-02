a = int(input())
b = int(input())
c = b
print("Before:")
print(f"a = {a}")
print(f"b = {b}")

c = a
a = b

print("After:")
print(f"a = {a}")
print(f"b = {c}")

