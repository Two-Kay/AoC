data = open("2021\Day5\input", "r+")
data = data.read()
data = data.split("\n")
start = []
end = []
for i in range(len(data)):
    tmp = data[i].split(" ")
    start.append(tmp[0].split(","))
    start[i][0] = int(start[i][0])
    start[i][1] = int(start[i][1])
    end.append(tmp[2].split(","))
    end[i][0] = int(end[i][0])
    end[i][1] = int(end[i][1])


def generate_sea_map(start, end):
    first_counter = 0
    second_counter = 0
    map = [[]]
    startx = []
    starty = []
    endx = []
    endy = []
    for i in range(len(start)):
        startx.append(start[i][0])
        starty.append(start[i][1])
        endx.append(end[i][0])
        endy.append(end[i][1])
    maxX = 0
    maxY = 0
    if(max(startx) > max(endx)):
        maxX = max(startx)
    else:
        maxX = max(endx)
    if(max(starty) > max(endy)):
        maxY = max(starty)
    else:
        maxY = max(endy)
    for x in range(maxX+1):
        map.append([])
        for y in range(maxY+1):
            map[x].append("-")

    for i in range(len(startx)):
        if(startx[i] == endx[i]):
            for j in range(len(map[0])):
                if(starty[i] < endy[i]):
                    if(j >= starty[i] and j <= endy[i]):
                        if(map[endx[i]][j] == "1"):
                            map[endx[i]][j] = "2"
                            first_counter += 1
                        elif(map[endx[i]][j] == "-"):
                            map[endx[i]][j] = "1"
                else:
                    if(j <= starty[i] and j >= endy[i]):
                        if(map[endx[i]][j] == "1"):
                            map[endx[i]][j] = "2"
                            first_counter += 1
                        elif(map[endx[i]][j] == "-"):
                            map[endx[i]][j] = "1"
        elif(starty[i] == endy[i]):
            for j in range(len(map)):
                if(startx[i] < endx[i]):
                    if(j >= startx[i] and j <= endx[i]):
                        if(map[j][endy[i]] == "1"):
                            map[j][endy[i]] = "2"
                            first_counter += 1
                        elif(map[j][endy[i]] == "-"):
                            map[j][endy[i]] = "1"
                else:
                    if(j <= startx[i] and j >= endx[i]):
                        if(map[j][endy[i]] == "1"):
                            map[j][endy[i]] = "2"
                            first_counter += 1
                        elif(map[j][endy[i]] == "-"):
                            map[j][endy[i]] = "1"
        else:
            iterations = 0
            if(startx[i] > endx[i]):
                iterations = startx[i]-endx[i]
                if(starty[i] > endy[i]):
                    for a in range(iterations+1):
                        if(map[endx[i] + a][endy[i] + a] == "1"):
                            map[endx[i] + a][endy[i] + a] = "2"
                            second_counter += 1
                        elif(map[endx[i] + a][endy[i] + a] == "-"):
                            map[endx[i] + a][endy[i] + a] = "1"
                else:
                    for a in range(iterations+1):
                        if(map[endx[i] + a][endy[i] - a] == "1"):
                            map[endx[i] + a][endy[i] - a] = "2"
                            second_counter += 1
                        elif(map[endx[i] + a][endy[i] - a] == "-"):
                            map[endx[i] + a][endy[i] - a] = "1"
            else:
                iterations = endx[i]-startx[i]
                if(starty[i] > endy[i]):
                    for a in range(iterations+1):
                        if(map[endx[i] - a][endy[i] + a] == "1"):
                            map[endx[i] - a][endy[i] + a] = "2"
                            second_counter += 1
                        elif(map[endx[i] - a][endy[i] + a] == "-"):
                            map[endx[i] - a][endy[i] + a] = "1"
                else:
                    for a in range(iterations+1):
                        if(map[endx[i] - a][endy[i] - a] == "1"):
                            map[endx[i] - a][endy[i] - a] = "2"
                            second_counter += 1
                        elif(map[endx[i] - a][endy[i] - a] == "-"):
                            map[endx[i] - a][endy[i] - a] = "1"
    second_counter += first_counter
    return first_counter, second_counter


puzzle1, puzzle2 = generate_sea_map(start, end)
print(puzzle2)
    
