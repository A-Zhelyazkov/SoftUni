percentage = int(input())


def loading_bar(n):
    times_percentage = percentage // 10
    bar = []
    for i in range(1, 11):
        if times_percentage > 0:
            bar.append("%")
            times_percentage -= 1
        else:
            bar.append(".")

    if percentage == 100:
        print(f"{percentage}% Complete!")
        print(f"[{''.join(bar)}]")
    else:
        print(f"{percentage}% [{''.join(bar)}]")
        print(f"Still loading...")


loading_bar(percentage)

