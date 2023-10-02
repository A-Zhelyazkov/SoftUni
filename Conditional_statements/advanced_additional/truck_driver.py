season = input()
kilometers_per_month = float(input())
gross_salary = 0

if kilometers_per_month <= 5000:
    if season == "Autumn" or season == "Spring":
        gross_salary = (0.75 * kilometers_per_month) * 4
    elif season == "Summer":
        gross_salary = (0.9 * kilometers_per_month) * 4
    elif season == "Winter":
        gross_salary = (1.05 * kilometers_per_month) * 4

elif kilometers_per_month <= 10000:
    if season == "Autumn" or season == "Spring":
        gross_salary = (0.95 * kilometers_per_month) * 4
    elif season == "Summer":
        gross_salary = (1.1 * kilometers_per_month) * 4
    elif season == "Winter":
        gross_salary = (1.25 * kilometers_per_month) * 4

elif kilometers_per_month <= 20000:
        gross_salary = (1.45 * kilometers_per_month) * 4

net_salary = gross_salary * 0.9
print(f"{net_salary:.2f}")
