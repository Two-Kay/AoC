file = "2023/Day10/input"


def pathfindy(file):
    output = 0
    grid = []
    start = []
    marked_coords = []
    step = 0
    marked_grid = []
    to_north = {"L", "J", "|", 0}
    to_south = {"7", "F", "|", 0}
    to_west = {"-", "7", "J", 0}
    to_east = {"-", "F", "L", 0}
    with open(file, "r+") as f:
        i = 0
        for line in f:
            grid.append(list(line.strip("\n")))
            marked_grid.append(list(line.strip("\n")))
            try:
                start = [i, line.index("S")]
                marked_coords = [[i, start[1]]]
                marked_grid[i][start[1]] = 0
            except ValueError:
                pass
            i += 1

    while len(marked_coords) > 0:
        new_marked_coords = []
        for marked_coord in marked_coords:
            y, x = marked_coord
            if y > 0 and marked_grid[y][x] in to_north and marked_grid[y-1][x] in to_south:
                new_marked_coords.append([y-1, x])
            if y < len(grid) - 1 and marked_grid[y][x] in to_south and marked_grid[y+1][x] in to_north:
                new_marked_coords.append([y+1, x])
            if x > 0 and marked_grid[y][x] in to_west and marked_grid[y][x-1] in to_east:
                new_marked_coords.append([y, x-1])
            if x < len(grid[0]) - 1 and marked_grid[y][x] in to_east and marked_grid[y][x+1] in to_west:
                new_marked_coords.append([y, x+1])
            marked_grid[y][x] = step
        step += 1
        marked_coords = new_marked_coords
    return step - 1


print(pathfindy(file))
