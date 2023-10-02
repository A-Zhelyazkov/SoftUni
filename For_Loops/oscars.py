actor_name = input()
academy_points = float(input())
count_judge = int(input())
points = academy_points

for i in range(count_judge):
    name_judge = input()
    judge_points = float(input())
    points += (len(name_judge) * judge_points) / 2
    if points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break

if points < 1250.5:
    diff = 1250.5 - points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
