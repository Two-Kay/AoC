file = "2023/Day6/input"


def race(file):
    race_data = []
    output = 1
    with open(file, "r+") as f:
        for line in f:
            modified = line.strip().split(" ")
            new_line = []
            for element in modified:
                try:
                    new_line.append(int(element))
                except:
                    continue
            race_data.append(new_line)
    for j in range(len(race_data[0])):
        wins = 0
        for i in range(race_data[0][j]):
            distance = i * (race_data[0][j] - i)
            if distance > race_data[1][j]:
                wins += 1
        output *= wins
    return output


def one_race(file):
    race_data = []
    output = 1
    with open(file, "r+") as f:
        for line in f:
            race_data.append(line.strip().replace(" ", "").split(":")[1])
    wins = 0
    for i in range(int(race_data[0])):
        distance = i * (int(race_data[0]) - i)
        if distance > int(race_data[1]):
            wins += 1
    output *= wins
    return output


print(race(file))
print(one_race(file))
