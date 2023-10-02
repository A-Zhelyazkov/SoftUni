def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"

    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for symbol in winning_symbols:
        for consecutive_symbol in range(10, 5, -1):
            repetitions = consecutive_symbol * symbol
            if repetitions in left_part and repetitions in right_part:
                if len(repetitions) == 10:
                    return f'ticket "{ticket}" - {consecutive_symbol}{symbol} Jackpot!'
                else:
                    return f'ticket "{ticket}" - {consecutive_symbol}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [i.strip() for i in input().split(", ")]
for ticket in tickets:
    print(is_winning(ticket))