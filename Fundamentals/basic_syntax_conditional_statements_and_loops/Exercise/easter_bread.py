budget = float(input())
flour = float(input())

eggs = flour * 0.75
milk = (flour * 1.25) / 4
price_per_loaf = flour + eggs + milk
colored_eggs = 0
loaves_made = 0
while price_per_loaf <= budget:
    budget -= price_per_loaf
    loaves_made += 1
    colored_eggs += 3

    if loaves_made % 3 == 0:
        colored_eggs -= (loaves_made - 2)

print(f"You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

