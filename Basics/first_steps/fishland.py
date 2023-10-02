skumriq_price_kg = float(input())
caca_price_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price_kg = skumriq_price_kg + (skumriq_price_kg * 0.6)
safrid_price_kg = caca_price_kg + (caca_price_kg * 0.8)
midi_price_kg = 7.50

total_palamud = palamud_price_kg * palamud_kg
total_safrid = safrid_kg * safrid_price_kg
total_midi = midi_kg * midi_price_kg
total_bill = total_midi + total_safrid + total_palamud
print(f'{total_bill:.2f}')

