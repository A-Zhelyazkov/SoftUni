from collections import deque

total_food = deque([int(i) for i in input().split(", ")])
total_stamina = deque([int(i) for i in input().split(", ")])

peaks = []
counter = 0

while total_stamina and total_food:
    food = total_food.pop()
    stamina = total_stamina.popleft()
    counter += 1

    curr_sum = food + stamina

    if counter == 1 and curr_sum >= 80:
        peaks.append("Vihren")
    elif counter == 2 and curr_sum >= 90:
        peaks.append("Kutelo")
    elif counter == 3 and curr_sum >= 100:
        peaks.append("Banski Suhodol")
    elif counter == 4 and curr_sum >= 60:
        peaks.append("Polezhan")
    elif counter == 5 and curr_sum >= 70:
        peaks.append("Kamenitza")
    else:
        counter -= 1

set_peaks = set(peaks)

if len(set_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks:
    print("Conquered peaks:")
    for peak in peaks:
        print(peak)
