file = "2023/Day2/input"


def bag_of_colors(file):
    colors = {"red": 12, "green": 13, "blue": 14}
    output = 0
    with open(file, "r+") as f:
        for row in f:
            colors_game = {
                "red": colors["red"], "green": colors["green"], "blue": colors["blue"]}
            game = row.strip().split(" ")
            id = game[1]
            id = id.split(":")[0]
            bag_of_colors = game[2:]
            i = 1
            is_possible = True
            while i < len(bag_of_colors):
                reset = False
                if ";" in bag_of_colors[i]:
                    reset = True
                    bag_of_colors[i] = bag_of_colors[i].split(";")[0]
                else:
                    bag_of_colors[i] = bag_of_colors[i].split(",")[0]
                if bag_of_colors[i] == "red":
                    colors_game["red"] -= int(bag_of_colors[i-1])
                elif bag_of_colors[i] == "green":
                    colors_game["green"] -= int(bag_of_colors[i-1])
                elif bag_of_colors[i] == "blue":
                    colors_game["blue"] -= int(bag_of_colors[i-1])
                if reset:
                    if not (colors_game["red"] >= 0 and colors_game["blue"] >= 0 and colors_game["green"] >= 0):
                        is_possible = False
                    colors_game = {
                        "red": colors["red"], "green": colors["green"], "blue": colors["blue"]}
                i += 2
            if not (colors_game["red"] >= 0 and colors_game["blue"] >= 0 and colors_game["green"] >= 0):
                is_possible = False
            if is_possible:
                output += int(id)

        return output


def power_of_cubes(file):
    output = 0
    with open(file, "r+") as f:
        for row in f:
            game = row.split(":")
            id = game[0].split(" ")[1].strip(":")
            bags_raw = game[1].split(";")
            bags = []
            for bag in bags_raw:
                new_bags = bag.strip().split(",")
                for i in range(len(new_bags)):
                    new_bags[i] = new_bags[i].strip(" ").split(" ")
                bags.append(new_bags)
            minimum_colors = {"red": 0, "green": 0, "blue": 0}
            for bag in bags:
                for cube in bag:
                    if minimum_colors[cube[1]] <= int(cube[0]):
                        minimum_colors[cube[1]] = int(cube[0])
            power = 1
            for key in minimum_colors:
                power *= minimum_colors[key]
            output += power
        return output


print(bag_of_colors(file))
print(power_of_cubes(file))
