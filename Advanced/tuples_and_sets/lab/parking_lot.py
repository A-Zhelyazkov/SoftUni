n = int(input())

reg_plates = set()

for _ in range(n):
    action, plate = input().split(", ")

    if action == "IN":
        reg_plates.add(plate)

    elif action == "OUT":
        if plate in reg_plates:
            reg_plates.remove(plate)
        else:
            continue

if reg_plates:
    for plate in reg_plates:
        print(plate)
else:
    print("Parking Lot is Empty")
