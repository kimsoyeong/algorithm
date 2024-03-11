T = int(input())

for test_case in range(1, T + 1):
    ln = input().strip()

    cards = {
        'S': [],
        'D': [],
        'H': [],
        'C': []
    }

    for i in range(0, len(ln), 3):
        card_shape = ln[i]
        card_number = ln[i + 1: i + 3]

        if card_number in cards[card_shape]:
            print(f"#{test_case} ERROR")
            break
        else:
            cards[card_shape].append(card_number)
    else:
        print(f"#{test_case}", end=" ")
        for s in ['S', 'D', 'H', 'C']:
            print(13 - len(cards[s]), end=" ")
        print()
