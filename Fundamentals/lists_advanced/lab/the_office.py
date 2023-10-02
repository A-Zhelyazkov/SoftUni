happiness_list = [int(i) for i in input().split()]
factor = int(input())
multiplied_list = [i*factor for i in happiness_list]

average_happiness = sum(multiplied_list) / len(multiplied_list)
happy_people = [i for i in multiplied_list if i >= average_happiness]

if len(happy_people) >= len(multiplied_list) / 2:
    print(f"Score: {len(happy_people)}/{len(multiplied_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy_people)}/{len(multiplied_list)}. Employees are not happy!")

