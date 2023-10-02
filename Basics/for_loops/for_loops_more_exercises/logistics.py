cargos = int(input())

mini_bus_total = 0
truck_total = 0
train_total = 0
total_cargo = 0
tons_bus = 0
tons_truck = 0
tons_train = 0
for i in range(cargos):
    tons = int(input())
    total_cargo += tons
    if tons <= 3:
        tons_bus += tons
        mini_bus_total += tons * 200
    elif tons <= 11:
        tons_truck += tons
        truck_total += tons * 175
    elif tons >= 12:
        tons_train += tons
        train_total += tons * 120


average_expense = (train_total + truck_total + mini_bus_total) / total_cargo
average_bus = (tons_bus / total_cargo) * 100
average_truck = (tons_truck / total_cargo) * 100
average_train = (tons_train / total_cargo) * 100

print(f"{average_expense:.2f}")
print(f"{average_bus:.2f}%")
print(f"{average_truck:.2f}%")
print(f"{average_train:.2f}%")

