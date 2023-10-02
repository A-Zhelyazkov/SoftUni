first_num = int(input())
second_num = int(input())
third_num = int(input())


for first in range(1, first_num + 1):
    for second in range(2, second_num + 1):
        counter = 0
        for n in range(1, second + 1):
            if second % n == 0:
                counter += 1
        if counter > 2:
            continue
        for third in range(1, third_num + 1):
            if first % 2 == 0 and third % 2 == 0:
                print(f"{first} {second} {third}")