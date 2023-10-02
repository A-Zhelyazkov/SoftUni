n = int(input())
heroes = {}
for _ in range(n):
    data = input().split()
    hero = data[0]
    hp = int(data[1])
    mp = int(data[2])
    hp = min(hp, 100)
    mp = min(mp, 200)
    heroes[hero] = {'hp': hp, 'mp': mp}

while True:
    data = input()

    if data == "End":
        break

    data_args = data.split(" - ")
    action = data_args[0]
    hero = data_args[1]

    if action == "CastSpell":
        mp_needed = int(data_args[2])
        spell_name = data_args[3]
        if heroes[hero]['mp'] >= mp_needed:
            heroes[hero]['mp'] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mp']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(data_args[2])
        attacker = data_args[3]
        heroes[hero]['hp'] -= damage
        if heroes[hero]['hp'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes[hero]

    elif action == "Recharge":
        amount = int(data_args[2])
        if heroes[hero]['mp'] + amount <= 200:
            heroes[hero]['mp'] += amount
            print(f"{hero} recharged for {amount} MP!")
        else:
            print(f"{hero} recharged for {200 - heroes[hero]['mp']} MP!")
            heroes[hero]['mp'] = 200

    elif action == "Heal":
        amount = int(data_args[2])
        if heroes[hero]['hp'] + amount <= 100:
            heroes[hero]['hp'] += amount
            print(f"{hero} healed for {amount} HP!")
        else:
            print(f"{hero} healed for {100 - heroes[hero]['hp']} HP!")
            heroes[hero]['hp'] = 100


for hero, values in heroes.items():
    print(f"{hero}")
    print(f"  HP: {values['hp']}")
    print(f"  MP: {values['mp']}")