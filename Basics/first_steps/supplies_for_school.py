pens = int(input("Pen Packets: "))
markers = int(input("Marker Packets: "))
cleaning_detergent = int(input("Litres of Cleaning Detergent: "))
discount = int(input("Discount: "))
price_for_pens = pens * 5.80
price_for_markers = markers * 7.20
price_for_detergent = cleaning_detergent * 1.20
total_sum = price_for_detergent + price_for_pens + price_for_markers
discounted_price = total_sum -  (total_sum * (discount / 100))
print(discounted_price)

