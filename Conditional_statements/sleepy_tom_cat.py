total_weekend = int(input())

total_work_days = 365 - total_weekend

total_play_time = (total_work_days * 63) + (total_weekend * 127)
norm = 30000
play_norm = abs(30000 - total_play_time)
hours_play = play_norm // 60
minutes_play = play_norm % 60

if total_play_time > norm:
    print("Tom will run away")
    print(f"{hours_play} hours and {minutes_play} minutes more for play")
if total_play_time <= norm:
    print("Tom sleeps well")
    print(f"{hours_play} hours and {minutes_play} minutes less for play")
