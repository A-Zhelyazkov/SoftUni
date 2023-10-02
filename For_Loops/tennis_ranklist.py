import math

tournaments = int(input())
starting_points = int(input())
total_wins = 0

points = starting_points

for i in range(tournaments):
    position = input()
    if position == "W":
        total_wins += 1
        points += 2000
    elif position == "F":
        points += 1200
    elif position == "SF":
        points += 720

average_points = math.floor((points - starting_points) / tournaments)
percent_tournaments_won = (total_wins / tournaments) * 100

print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{percent_tournaments_won:.2f}%")
