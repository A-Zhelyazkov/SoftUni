from collections import deque

textiles = deque([int(i) for i in input().split()])
meds = deque([int(i) for i in input().split()])
final_items = {"MedKit": 0, "Bandage": 0, "Patch": 0}

while textiles and meds:
    textile = textiles.popleft()
    med = meds.pop()

    curr_sum = textile + med

    if curr_sum == 30:
        final_items["Patch"] += 1
    elif curr_sum == 40:
        final_items["Bandage"] += 1
    elif curr_sum == 100:
        final_items["MedKit"] += 1
    else:
        if curr_sum < 100:
            med += 10
            meds.append(med)
        else:
            over = curr_sum - 100
            final_items["MedKit"] += 1
            meds[-1] += over

if not textiles and not meds:
    print(f"Textiles and medicaments are both empty.")
elif not textiles:
    print(f"Textiles are empty.")
elif not meds:
    print(f"Medicaments are empty.")

final_items = sorted(final_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for key, value in final_items:
    if value != 0:
        print(f"{key} - {value}")

if textiles:
    print(f"Textiles left: {', '.join(str(i) for i in textiles)}")
if meds:
    meds = reversed(meds)
    print(f"Medicaments left: {', '.join(str(i) for i in meds)}")