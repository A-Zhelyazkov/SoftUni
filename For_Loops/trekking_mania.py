total_groups = int(input())
musala_groups = 0
monblan_groups = 0
kilimanjaro_groups = 0
k2_groups = 0
everest_groups = 0
total_people = 0

for i in range(total_groups):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        musala_groups += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan_groups += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimanjaro_groups += people_in_group
    elif 26 <= people_in_group <= 40:
        k2_groups += people_in_group
    elif people_in_group >= 41:
        everest_groups += people_in_group

percent_musala = (musala_groups / total_people) * 100
percent_monblan = (monblan_groups / total_people) * 100
percent_kilimanjaro = (kilimanjaro_groups / total_people) * 100
percent_k2 = (k2_groups / total_people) * 100
percent_everest = (everest_groups / total_people) * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")

