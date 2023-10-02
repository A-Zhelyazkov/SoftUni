hour_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())

time_of_exam = (hour_exam * 60) + minutes_exam
time_of_arrival = (hour_arrival * 60) + minutes_arrival
late = time_of_arrival - time_of_exam
early = time_of_exam - time_of_arrival

# if late below 1 hr
minutes_late = time_of_arrival - time_of_exam
# if late above 1 hr
hours_late = (time_of_arrival - time_of_exam) // 60
hours_minutes_late = (time_of_arrival - time_of_exam) % 60

# if early below 1 hr
minutes_early = time_of_exam - time_of_arrival
# if early above 1 hr
hours_early = (time_of_exam - time_of_arrival) // 60
hours_minutes_early = (time_of_exam - time_of_arrival) % 60

if time_of_exam < time_of_arrival:
    print("Late")
    if late < 60:
        print(f"{minutes_late} minutes after the start")
    if late >= 60:
        if hours_minutes_late <= 9:
            print(f"{hours_late}:0{hours_minutes_late} hours after the start")
        else:
            print(f"{hours_late}:{hours_minutes_late} hours after the start")

elif time_of_exam == time_of_arrival:
    print("On time")

elif early <= 30:
    print("On time")
    print(f"{minutes_early} minutes before the start")

elif 60 > early > 30:
    print("Early")
    print(f"{minutes_early} minutes before the start")

elif early >= 60:
    print("Early")
    if hours_minutes_early <= 9:
        print(f"{hours_early}:0{hours_minutes_early} hours before the start")
    else:
        print(f"{hours_early}:{hours_minutes_early} hours before the start")