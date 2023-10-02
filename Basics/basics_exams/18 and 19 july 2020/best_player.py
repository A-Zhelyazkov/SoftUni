best_player = ""
goals_player = 0
while True:
    player_name = input()
    if player_name == "END":
        break
    goals = int(input())

    if goals > goals_player:
        best_player = player_name
        goals_player = goals
    if goals >= 10:
        break

print(f"{best_player} is the best player!")
if goals_player >= 3:
    print(f"He has scored {goals_player} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals_player} goals.")


