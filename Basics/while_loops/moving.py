width = int(input())
length = int(input())
height = int(input())

volume = width * length * height
total_taken_space = 0
operation = input()
flag = False

while operation != "Done":
    boxes = int(operation)
    total_taken_space += boxes
    if total_taken_space > volume:
        flag = True
        break
    operation = input()

diff = abs(volume - total_taken_space)
if flag:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")