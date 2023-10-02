def gather_credits(n, *args):
    taken_courses = []
    total_credits = 0
    result = ""
    for course, c_credits in args:
        if total_credits < n:
            if course not in taken_courses:
                total_credits += c_credits
                taken_courses.append(course)
        else:
            break

    if total_credits >= n:
        result += f"Enrollment finished! Maximum credits: {total_credits}.\n"
        taken_courses = sorted(taken_courses)
        result += f"Courses: {', '.join(taken_courses)}"

    else:
        result += f"You need to enroll in more courses! You have to gather {n - total_credits} credits more."

    return result

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))


