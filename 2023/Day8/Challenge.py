file = "2023/Day8/test_input_2"


def directions(file):
    output = 0
    is_header = True
    directions = ""
    places = {}
    with open(file, "r+") as f:
        for line in f:
            if is_header:
                directions = line.strip()
                is_header = False
            else:
                if len(line) > 1:
                    split = line.strip().split(" = ")
                    split[1] = split[1].strip("(")
                    split[1] = split[1].strip(")")
                    move = split[1].split(", ")
                    places[split[0]] = move
    current_name = "AAA"
    i = 0
    while current_name != "ZZZ":
        if directions[i] == "R":
            current_name = places[current_name][1]
        else:
            current_name = places[current_name][0]
        output += 1
        i += 1
        if i == len(directions):
            i = 0
    return output


print(directions(file))
