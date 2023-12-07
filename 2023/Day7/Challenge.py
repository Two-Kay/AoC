file = "2023/Day7/input"


def camel_cards(file):
    output = 0
    hands = []
    with open(file, "r+") as f:
        for line in f:
            hands.append(line.strip().split(" "))
    for hand in hands:
        cards = hand[0][::-1]
        card_value = 0
        matches = []
        checked = []
        for i in range(len(cards)):
            if cards[i] == "3":
                card_value += 1 * (100**i)
            if cards[i] == "4":
                card_value += 2 * (100**i)
            if cards[i] == "5":
                card_value += 3 * (100**i)
            if cards[i] == "6":
                card_value += 4 * (100**i)
            if cards[i] == "7":
                card_value += 5 * (100**i)
            if cards[i] == "8":
                card_value += 6 * (100**i)
            if cards[i] == "9":
                card_value += 7 * (100**i)
            if cards[i] == "T":
                card_value += 8 * (100**i)
            if cards[i] == "J":
                card_value += 9 * (100**i)
            if cards[i] == "Q":
                card_value += 10 * (100**i)
            if cards[i] == "K":
                card_value += 12 * (100**i)
            if cards[i] == "A":
                card_value += 13 * (100**i)
            if cards[i] not in checked:
                found = False
                for match in matches:
                    if len(match) > 0 and cards[i] in match:
                        match.append(cards[i])
                        found = True
                if not found:
                    checked.append(cards[i])
            else:
                matches.append([cards[i]])
                new_checked = []
                for card in checked:
                    if card == matches[len(matches) - 1][0]:
                        matches[len(matches) - 1].append(card)
                    else:
                        new_checked.append(card)
                checked = new_checked
        if len(checked) == 5:
            card_value += 1 * (100**5)
        elif len(matches) == 1:
            if len(matches[0]) == 2:
                card_value += 2 * (100**5)
            elif len(matches[0]) == 3:
                card_value += 4 * (100**5)
            elif len(matches[0]) == 4:
                card_value += 6 * (100**5)
            elif len(matches[0]) == 5:
                card_value += 7 * (100**5)
        elif len(matches) == 2:
            if len(matches[0]) == 2 and len(matches[1]) == 2:
                card_value += 3 * (100**5)
            else:
                card_value += 5 * (100**5)
        hand.append(card_value)
    hands.sort(key=lambda x: x[2])
    for i, hand in enumerate(hands):
        output += int(hand[1]) * (i + 1)
    return output


def joker(file):
    output = 0
    hands = []
    with open(file, "r+") as f:
        for line in f:
            hands.append(line.strip().split(" "))
    for hand in hands:
        cards = hand[0][::-1]
        card_value = 0
        matches = []
        checked = []
        jokers = []
        for i in range(len(cards)):
            if cards[i] == "2":
                card_value += 1 * (100**i)
            if cards[i] == "3":
                card_value += 2 * (100**i)
            if cards[i] == "4":
                card_value += 3 * (100**i)
            if cards[i] == "5":
                card_value += 4 * (100**i)
            if cards[i] == "6":
                card_value += 5 * (100**i)
            if cards[i] == "7":
                card_value += 6 * (100**i)
            if cards[i] == "8":
                card_value += 7 * (100**i)
            if cards[i] == "9":
                card_value += 8 * (100**i)
            if cards[i] == "T":
                card_value += 9 * (100**i)
            if cards[i] == "Q":
                card_value += 10 * (100**i)
            if cards[i] == "K":
                card_value += 12 * (100**i)
            if cards[i] == "A":
                card_value += 13 * (100**i)
            if cards[i] == "J":
                jokers.append(cards[i])
            elif cards[i] not in checked:
                found = False
                for match in matches:
                    if len(match) > 0 and cards[i] in match:
                        match.append(cards[i])
                        found = True
                if not found:
                    checked.append(cards[i])
            else:
                matches.append([cards[i]])
                new_checked = []
                for card in checked:
                    if card == matches[len(matches) - 1][0]:
                        matches[len(matches) - 1].append(card)
                    else:
                        new_checked.append(card)
                checked = new_checked
        if len(checked) == 5:
            card_value += 1 * (100**5)
        elif len(jokers) > 0 and len(matches) == 0:
            if len(jokers) == 1:
                card_value += 2 * (100**5)
            elif len(jokers) == 2:
                card_value += 4 * (100**5)
            elif len(jokers) == 3:
                card_value += 6 * (100**5)
            elif len(jokers) > 3:
                card_value += 7 * (100**5)
        elif len(matches) == 1:
            if (len(matches[0]) + len(jokers)) == 5:
                card_value += 7 * (100**5)
            elif (len(matches[0]) + len(jokers)) == 4:
                card_value += 6 * (100**5)
            elif len(jokers) == 3 or (len(jokers) == 2 and len(matches[0]) == 3):
                card_value += 5 * (100**5)
            elif (len(matches[0]) + len(jokers)) == 3:
                card_value += 4 * (100**5)
            elif (len(matches[0])) == 2:
                card_value += 2 * (100**5)
        elif len(matches) == 2:
            if len(matches[0]) == 2 and len(matches[1]) == 2 and len(jokers) == 0:
                card_value += 3 * (100**5)
            else:
                card_value += 5 * (100**5)
        hand.append(card_value)
    hands.sort(key=lambda x: x[2])
    for i, hand in enumerate(hands):
        output += int(hand[1]) * (i + 1)
    return output


print(camel_cards(file))
print(joker(file))
