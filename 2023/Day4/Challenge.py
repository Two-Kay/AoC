file = "2023/Day4/input"


def remove_empty(numbers):
    output = []
    for number in numbers:
        if len(number) > 0:
            output.append(number)
    return output


def scratch_cards(file):
    output = 0
    with open(file, "r+") as f:
        for card in f:
            winning = 0
            card = card.split("\n")[0].split(f": ")[1]
            winning_numbers = remove_empty(card.split(" | ")[0].split(" "))
            numbers = remove_empty(card.split(" | ")[1].split(" "))
            for winning_number in winning_numbers:
                if winning_number in numbers:
                    if winning == 0:
                        winning += 1
                    else:
                        winning *= 2
            output += winning
    return output


def unlimited_scratchcards(file):
    output = 0
    card_dict = {}
    to_process = []
    with open(file, "r+") as f:
        i = 1
        for card in f:
            to_process.append(i)
            card = card.split("\n")[0].split(f": ")[1]
            winning_numbers = remove_empty(card.split(" | ")[0].split(" "))
            numbers = remove_empty(card.split(" | ")[1].split(" "))
            card_dict[i] = [winning_numbers, numbers]
            i += 1
    for process in to_process:
        output += 1
        won = 0
        for winning_number in card_dict[process][0]:
            if winning_number in card_dict[process][1]:
                won += 1
                to_process.append(process+won)
    return output


print(scratch_cards(file))
print(unlimited_scratchcards(file))
