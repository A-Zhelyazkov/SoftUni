from math import ceil
series = input()
episode_length = int(input())
break_length = int(input())

lunch = break_length / 8
relax = break_length / 4
remaining_break = break_length - (lunch + relax)
diff = abs(remaining_break - episode_length)
if remaining_break >= episode_length:
    print(f"You have enough time to watch {series} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(diff)} more minutes.")