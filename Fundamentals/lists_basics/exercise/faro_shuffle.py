cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    final_list = []
    half_deck = len(cards) // 2
    first_half = cards[:half_deck]
    second_half = cards[half_deck:]
    for i in range(len(first_half)):
        final_list.append(first_half[i])
        final_list.append(second_half[i])
    cards = final_list
print(cards)

