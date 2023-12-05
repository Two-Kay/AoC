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


# def many_seeds(file):
#     import math
#     output = math.inf
#     seeds = []
#     maps = []
#     new_map = []
#     first = True
#     with open(file, "r+") as f:
#         for line in f:
#             if first:
#                 seeds = line.split("seeds:")[1].strip().split(" ")
#                 first = False
#             else:
#                 if "map:" in line:
#                     if len(new_map) > 0:
#                         maps.append(new_map)
#                     new_map = []
#                 elif len(line) > 1:
#                     new_map.append(line.strip("\n").split(" "))
#         maps.append(new_map)

#     seed_ranges = {}
#     first = True
#     for i in range(len(seeds)):
#         if first:
#             for j in range(int(seeds[i+1])):
#                 seed_ranges[int(seeds[i]) + j] = 0
#         first = not first
#     run = 0
#     for seed in seed_ranges:
#         val = int(seed)
#         for map in maps:
#             for conv in map:
#                 if val >= int(conv[1]) and val < (int(conv[1]) + int(conv[2])):
#                     val = int(conv[0]) + val - int(conv[1])
#                     break
#         if val < output:
#             output = val
#         run += 1
#         if run % 1000 == 0:
#             print(f"{run}/{len(seed_ranges)}")
#     return output


print(ferilizer(file))
