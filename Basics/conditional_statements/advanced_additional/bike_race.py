juniors = int(input())
seniors = int(input())
track = input()
money_raised = 0

if track == "trail":
    money_raised = ((juniors * 5.50) + (seniors * 7)) * 0.95

elif track == "cross-country":
    if juniors + seniors >= 50:
        money_raised = (((juniors * 8 * 0.75) + (seniors * 9.5 * 0.75)) * 0.95)
    else:
        money_raised = ((juniors * 8) + (seniors * 9.5)) * 0.95

elif track == "downhill":
    money_raised = ((juniors * 12.25) + (seniors * 13.75)) * 0.95

elif track == "road":
    money_raised = ((juniors * 20) + (seniors * 21.50)) * 0.95

print(f"{money_raised:.2f}")
