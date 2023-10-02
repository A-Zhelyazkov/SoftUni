volume = int(input())
p1_debit = int(input())
p2_debit = int(input())
hours_missing = float(input())

# volume each pipe filling and both together
p1_volume_filled = p1_debit * hours_missing
p2_volume_filled = p2_debit * hours_missing
total_filled = p1_volume_filled + p2_volume_filled

# percentage each pipe of total
p1_percentage_filled = (p1_volume_filled / total_filled) * 100
p2_percentage_filled = (p2_volume_filled / total_filled) * 100

percentage_filled = (total_filled / volume) * 100

if total_filled <= volume:
    print(f"The pool is {percentage_filled}% full. Pipe 1: {round(p1_percentage_filled, 2)}%. Pipe 2: {round(p2_percentage_filled, 2)}%.")
else:
    overflow = abs(volume - total_filled)
    print(f"For {hours_missing} hours the pool overflows with {overflow} liters.")

