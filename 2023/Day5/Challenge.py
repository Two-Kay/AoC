file = "2023/Day5/input"


def ferilizer(file):
    import math
    output = math.inf
    seeds = []
    maps = []
    new_map = []
    first = True
    with open(file, "r+") as f:
        for line in f:
            if first:
                seeds = line.split("seeds:")[1].strip().split(" ")
                first = False
            else:
                if "map:" in line:
                    if len(new_map) > 0:
                        maps.append(new_map)
                    new_map = []
                elif len(line) > 1:
                    new_map.append(line.strip("\n").split(" "))
        maps.append(new_map)

    for seed in seeds:
        val = int(seed)
        for map in maps:
            for conv in map:
                if val >= int(conv[1]) and val < (int(conv[1]) + int(conv[2])):
                    val = int(conv[0]) + val - int(conv[1])
                    break
        if val < output:
            output = val
    return output


def solve_seed(seed, maps):
    for map in maps:
        for conv in map:
            if seed >= int(conv[1]) and seed < (int(conv[1]) + int(conv[2])):
                seed = int(conv[0]) + seed - int(conv[1])
                break
    return seed


def hill_climby(file):
    import math
    output = math.inf
    seeds = []
    maps = []
    new_map = []
    first = True
    with open(file, "r+") as f:
        for line in f:
            if first:
                seeds_list = line.split("seeds:")[1].strip().split(" ")
                for i in range(int(len(seeds_list) / 2)):
                    seeds.append([seeds_list[i*2], seeds_list[i*2 + 1]])
                first = False
            else:
                if "map:" in line:
                    if len(new_map) > 0:
                        maps.append(new_map)
                    new_map = []
                elif len(line) > 1:
                    new_map.append(line.strip("\n").split(" "))
        maps.append(new_map)
    import random
    for run in range(1000000):
        temp = 100
        seed_range = random.sample(seeds, 1)[0]
        val = random.randint(int(seed_range[0]), (int(
            seed_range[1]) + int(seed_range[0])))
        min = int(seed_range[0])
        max = int(seed_range[1]) + int(seed_range[0])
        hill_climb = solve_seed(val, maps)
        higher = math.inf
        if (val + 1) <= max:
            higher = solve_seed(val + 1, maps)
        if higher < hill_climb:
            val += 2
            hill_climb = higher
            while val <= max:
                higher = solve_seed(val, maps)
                if higher < hill_climb:
                    hill_climb = higher
                    i += 1
                else:
                    break
        else:
            smaller = math.inf
            if (val - 1) >= min:
                smaller = solve_seed(val - 1, maps)
            if smaller < hill_climb:
                val -= 2
                hill_climb = smaller
                while val >= min:
                    smaller = solve_seed(val, maps)
                    if smaller < hill_climb:
                        hill_climb = smaller
                        i -= 1
                    else:
                        break
        if hill_climb < output:
            output = hill_climb
    return output


def simulated_annealing(file):
    import math
    output = math.inf
    seeds = []
    maps = []
    new_map = []
    first = True
    with open(file, "r+") as f:
        for line in f:
            if first:
                seeds_list = line.split("seeds:")[1].strip().split(" ")
                for i in range(int(len(seeds_list) / 2)):
                    seeds.append([seeds_list[i*2], seeds_list[i*2 + 1]])
                first = False
            else:
                if "map:" in line:
                    if len(new_map) > 0:
                        maps.append(new_map)
                    new_map = []
                elif len(line) > 1:
                    new_map.append(line.strip("\n").split(" "))
        maps.append(new_map)
    import random
    for run in range(1000000):
        temp = 200
        seed_range = random.sample(seeds, 1)[0]
        val = random.randint(int(seed_range[0]), (int(
            seed_range[1]) + int(seed_range[0])))
        min = int(seed_range[0])
        max = int(seed_range[1]) + int(seed_range[0])
        hill_climb = solve_seed(val, maps)
        new_val = hill_climb
        while temp > 0 and new_val <= hill_climb:
            rand = random.randint(0, 1)

            if rand == 0 and (val + 1) <= max:
                higher = solve_seed(val + 1, maps)
                if higher <= hill_climb:
                    hill_climb = higher
                    i += 1
                else:
                    rand = random.randint(1, 100)
                    if rand < temp:
                        hill_climb = higher
                        i -= 1
                    temp -= (int(temp/10) + 1)
            elif rand == 1 and (val - 1) >= min:
                smaller = solve_seed(val - 1, maps)
                if smaller <= hill_climb:
                    hill_climb = smaller
                    i -= 1
                else:
                    rand = random.randint(1, 100)
                    if rand < temp:
                        hill_climb = smaller
                        i -= 1
                    temp -= (int(temp/10) + 1)

            else:
                break

        if hill_climb < output:
            output = hill_climb
    return output


def confirm(seeds, val):
    for seed in seeds:
        if val >= seed[0] and val <= (seed[0] + seed[1]):
            return True
    return False


def backtrack(file, confirmed_lowest):
    lowest = confirmed_lowest
    import math
    seeds = []
    maps = []
    new_map = []
    first = True
    with open(file, "r+") as f:
        for line in f:
            if first:
                seeds_list = line.split("seeds:")[1].strip().split(" ")
                for i in range(int(len(seeds_list) / 2)):
                    seeds.append(
                        [int(seeds_list[i*2]), int(seeds_list[i*2 + 1])])
                first = False
            else:
                if "map:" in line:
                    if len(new_map) > 0:
                        maps.append(new_map)
                    new_map = []
                elif len(line) > 1:
                    new_map.append(line.strip("\n").split(" "))
        maps.append(new_map)
    maps.reverse()
    lowest -= 1
    while lowest > (confirmed_lowest-10000):
        val = lowest
        for map in maps:
            for conv in map:
                if val >= int(conv[0]) and val < (int(conv[0]) + int(conv[2])):
                    val = int(conv[1]) + val - int(conv[0])
                    break
        if confirm(seeds, val):
            confirmed_lowest = lowest
        lowest -= 1
    return confirmed_lowest


def solve_tricksy_seed_optimizer(file):
    confirmed_lowest = simulated_annealing(file)
    return backtrack(file, confirmed_lowest)


print(ferilizer(file))
print(solve_tricksy_seed_optimizer(file))
