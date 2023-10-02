minutes_walking_day = int(input())
total_walks_day = int(input())
calories_intake = int(input())

total_walks_minutes = minutes_walking_day * total_walks_day
burnt_calories = total_walks_minutes * 5
half_the_taken_calories = calories_intake / 2

if half_the_taken_calories <= burnt_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burnt_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burnt_calories}.")