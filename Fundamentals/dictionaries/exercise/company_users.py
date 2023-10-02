companies = {}

while True:
    command = input()

    if command == "End":
        break

    company, id = command.split(" -> ")

    if company not in companies:
        companies[company] = []

    if id not in companies[company]:
        companies[company].append(id)

for company in companies:
    print(company)
    for value in companies[company]:
        print(f"-- {value}")
