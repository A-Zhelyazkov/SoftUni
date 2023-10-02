def students_credits(*args):
    total_credits = 0
    data = {}
    result = ''

    for line in args:
        subject, max_credits, max_points, points = line.split("-")
        max_credits = int(max_credits)
        max_points = int(max_points)
        points = int(points)
        got_credits = (points/max_points) * max_credits
        total_credits += got_credits
        data[subject] = got_credits

    data = sorted(data.items(), key=lambda x: -x[1])
    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    for course, credit in data:
        result += f"{course} - {credit:.1f}\n"

    return result

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
