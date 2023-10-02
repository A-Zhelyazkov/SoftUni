weight = float(input())
delivery_type = input()
distance = int(input())
total_sum = 0

if delivery_type == "standard":
    if weight < 1:
        total_sum = distance * 0.03
    elif weight < 10:
        total_sum = distance * 0.05
    elif weight < 40:
        total_sum = distance * 0.1
    elif weight < 90:
        total_sum = distance * 0.15
    elif weight < 150:
        total_sum = distance * 0.2

elif delivery_type == "express":
    if weight < 1:
        total_sum = distance * 0.03
        tax_weight = 0.03 * 0.8
        tax_km = tax_weight * weight
        tax_total = distance * tax_km
        total_sum += tax_total
    elif weight < 10:
        total_sum = distance * 0.05
        tax_weight = 0.05 * 0.4
        tax_km = tax_weight * weight
        tax_total = distance * tax_km
        total_sum += tax_total
    elif weight < 40:
        total_sum = distance * 0.1
        tax_weight = 0.1 * 0.05
        tax_km = tax_weight * weight
        tax_total = distance * tax_km
        total_sum += tax_total
    elif weight < 90:
        total_sum = distance * 0.15
        tax_weight = 0.15 * 0.02
        tax_km = tax_weight * weight
        tax_total = distance * tax_km
        total_sum += tax_total
    elif weight < 150:
        total_sum = distance * 0.2
        tax_weight = 0.2 * 0.01
        tax_km = tax_weight * weight
        tax_total = distance * tax_km
        total_sum += tax_total


print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_sum:.2f} lv.")
