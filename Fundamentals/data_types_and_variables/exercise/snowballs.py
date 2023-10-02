n = int(input())
best_snowball = 0
for i in range(n):
    snowball = 0
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball = (weight / time_needed) ** quality

    if snowball > best_snowball:
        best_weight = weight
        best_time = time_needed
        best_quality = quality
        best_snowball = snowball
print(f"{best_weight} : {best_time} = {int(best_snowball)} ({best_quality})")


