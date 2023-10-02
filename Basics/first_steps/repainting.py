nylon = int(input("Nylon(in sqr. meters): "))
paint = int(input("Litres of paint: "))
thinner = int(input("Litres of thinner: "))
work = int(input("Hours to finish: "))
sum_for_nylon = (nylon + 2) * 1.5
sum_for_paint = ((paint + (paint * 0.1)) * 14.5)
sum_for_thinner = thinner * 5
sum_for_bags = 0.4
total_sum_for_materials = sum_for_nylon + sum_for_paint + sum_for_thinner + sum_for_bags
sum_for_workers = (total_sum_for_materials * 0.3) * work
total_sum = total_sum_for_materials + sum_for_workers
print(total_sum)
