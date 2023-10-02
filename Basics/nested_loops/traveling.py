destination = input()
min_budget = float(input())
current_budget = 0

while destination != "End":
    savings = float(input())
    current_budget += savings
    if current_budget >= min_budget:
        print(f"Going to {destination}!")
        destination = input()
        if destination == "End":
            break
        min_budget = float(input())
        current_budget = 0
