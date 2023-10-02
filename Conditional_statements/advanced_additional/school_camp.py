season = input()
group_type = input()
students = int(input())
nights = int(input())
price = 0
sport = 0

if group_type == "girls" or group_type == "boys":
    if season == "Winter":
        if group_type == "boys":
            sport = "Judo"
        elif group_type == "girls":
            sport = "Gymnastics"
        elif group_type == "mixed":
            sport = "Ski"
        price = students * 9.6 * nights
    elif season == "Spring":
        if group_type == "boys":
            sport = "Tennis"
        elif group_type == "girls":
            sport = "Athletics"
        elif group_type == "mixed":
            sport = "Cycling"
        price = students * 7.2 * nights
    elif season == "Summer":
        if group_type == "boys":
            sport = "Football"
        elif group_type == "girls":
            sport = "Volleyball"
        elif group_type == "mixed":
            sport = "Swimming"
        price = students * 15 * nights

elif group_type == "mixed":
    if season == "Winter":
        sport = "Ski"
        price = students * 10 * nights
    elif season == "Spring":
        sport = "Cycling"
        price = students * 9.5 * nights
    elif season == "Summer":
        sport = "Swimming"
        price = students * 20 * nights

if students >= 50:
    price = price * 0.5
elif students >= 20:
    price = price * 0.85
elif students >= 10:
    price = price * 0.95

print(f"{sport} {price:.2f} lv.")
