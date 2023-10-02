t_shirt_price = float(input())
sum_for_ball = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.2
buttons = (t_shirt_price + shorts_price) * 2
bill = t_shirt_price + shorts_price + socks_price + buttons
discounted_bill = bill * 0.85

if discounted_bill >= sum_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {discounted_bill:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {sum_for_ball - discounted_bill:.2f} lv. more.")