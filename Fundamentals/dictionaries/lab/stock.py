input_line = input().split()
products = {}

for el in range(0, len(input_line), 2):
    key = input_line[el]
    value = int(input_line[el+1])
    products[key] = value

searches = input().split()

for el in searches:
    if el not in products:
        print(f"Sorry, we don't have {el}")
    else:
        print(f"We have {products[el]} of {el} left")

