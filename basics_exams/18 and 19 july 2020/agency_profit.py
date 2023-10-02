name = input()
tickets_adults = int(input())
tickets_kids = int(input())
price_ticket_adult = float(input())
tax_service = float(input())

price_ticket_kid = 0.3 * price_ticket_adult
price_ticket_adult_tax = price_ticket_adult + tax_service
price_ticket_kid_tax = price_ticket_kid + tax_service

total_price_adults = price_ticket_adult_tax * tickets_adults
total_price_kids = price_ticket_kid_tax * tickets_kids

total_profit = total_price_kids + total_price_adults
net_profit = total_profit * 0.2

print(f"The profit of your agency from {name} tickets is {net_profit:.2f} lv.")