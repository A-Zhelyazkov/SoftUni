materials = {"shards": 0, "fragments": 0, "motes": 0}
flag = False
while True:
    if flag:
        break
    input_line = input().split()
    counter = 0
    for i in range(len(input_line) // 2):
        material = input_line[counter+1].lower
        value = int(input_line[counter])
        if material() not in materials:
            materials[material()] = value
        else:
            materials[material()] += value
        counter += 2

        if "shards" in materials:
            if materials.get("shards") >= 250:
                print("Shadowmourne obtained!")
                materials["shards"] -= 250
                flag = True
                break

        if "fragments" in materials:
            if materials.get("fragments") >= 250:
                print("Valanyr obtained!")
                materials["fragments"] -= 250
                flag = True
                break

        if "motes" in materials:
            if materials.get("motes") >= 250:
                print("Dragonwrath obtained!")
                materials["motes"] -= 250
                flag = True
                break


for key, value in materials.items():
    print(f"{key}: {value}")