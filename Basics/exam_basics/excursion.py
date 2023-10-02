people = int(input())
nights = int(input())
cards_transport = int(input())
tickets_museums = int(input())

nights_cost = nights * 20
cards_transport_cost = cards_transport * 1.6
tickets_museums_cost = tickets_museums * 6
total_cost_person = nights_cost + cards_transport_cost + tickets_museums_cost

total_bill_without_tax = total_cost_person * people
bill_with_tax = total_bill_without_tax * 1.25

print(f"{bill_with_tax:.2f}")