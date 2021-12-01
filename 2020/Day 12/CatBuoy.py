def prepare(data):
    '''
    Splits input data into a list of directional operations as string
    and a list of distances/angles in integer.
    '''
    distances = []
    directions = []
    for i in range(len(data)):
        text = data[i]
        directions.append(text[0])
        distances.append(int(text[1:len(text)]))
    return (distances, directions)


data = open("Day 12\input12", "r+")
data = data.read()
data = data.split("\n")
distances, directions = prepare(data)


def move_ship(direction, distance):
    '''
    A function to move the ship according to its angle and direction.

    Returns the Manhattan distance taken since the beginning.
    '''
    directions = [0,0,0,0]
    degree = 90
    for i in range(len(direction)):
        if(direction[i] == "N"):
            directions[0] += distance[i]
        elif(direction[i] == "E"):
            directions[1] += distance[i]
        elif(direction[i] == "S"):
            directions[2] += distance[i]
        elif(direction[i] == "W"):
            directions[3] += distance[i]
        elif(direction[i] == "L"):
            degree -= distance[i]
            if(degree < 0):
                degree += 360
        elif(direction[i] == "R"):
            degree += distance[i]
            if(degree >= 360):
                degree -= 360
        elif(direction[i] == "F"):
            index = int(degree / 90)
            directions[index] += distance[i]

    northSouth = directions[0] - directions[2]
    westEast = directions[1] - directions[3]
    if(northSouth < 0):
        northSouth = northSouth * (-1)
    if(westEast < 0):
        westEast = westEast * (-1)

    return(northSouth+westEast)


def transform_directions(pos):
    '''
    A function to transform the direction values where the South/North
    and the East/West values would affect each other.

    Returns a new directions List.
    '''
    northSouth = []
    eastWest = []
    northSouth.append(pos[0])
    northSouth.append(pos[2])
    eastWest.append(pos[1])
    eastWest.append(pos[3])
    isNorth = northSouth[0] > northSouth[1]
    isEast = eastWest[0] > eastWest[1]
    posN = max(northSouth) - min(northSouth)
    posE = max(eastWest) - min(eastWest)
    
    ret = [0,0,0,0]
    if isNorth:
        ret[0] = posN
        ret[2] = 0
    else:
        ret[2] = posN
        ret[0] = 0
    if isEast:
        ret[1] = posE
        ret[3] = 0
    else:
        ret[3] = posE
        ret[1] = 0

    return ret


def move_waypoint(direction, distance):
    '''
    A function to direct waypoint around the ship and move the ship to its direction.
    The ship takes the distance of the waypoint buoy's coordinated multiplied by its forward operation value.

    Returns the Manhattan distance taken since the beginning.
    '''
    shipPos = [0,0,0,0]
    waypointPos = [1,10,0,0]
    for i in range(len(direction)):
        #print(i, shipPos, waypointPos, direction[i], distance[i])
        if(direction[i] == "N"):
            waypointPos[0] += distance[i]
        elif(direction[i] == "E"):
            waypointPos[1] += distance[i]
        elif(direction[i] == "S"):
            waypointPos[2] += distance[i]
        elif(direction[i] == "W"):
            waypointPos[3] += distance[i]
        
        waypointPos = transform_directions(waypointPos)

        if(direction[i] == "L"):
            degree = distance[i]
            count = int(degree / 90)
            while(count > 0):
                n = waypointPos[0]
                e = waypointPos[1]
                s = waypointPos[2]
                w = waypointPos[3]
                waypointPos[0] = e
                waypointPos[1] = s
                waypointPos[2] = w
                waypointPos[3] = n
                count -= 1
        elif(direction[i] == "R"):
            degree = distance[i]
            count = int(degree / 90)
            while(count > 0):
                n = waypointPos[0]
                e = waypointPos[1]
                s = waypointPos[2]
                w = waypointPos[3]
                waypointPos[0] = w
                waypointPos[1] = n
                waypointPos[2] = e
                waypointPos[3] = s
                count -= 1

        elif(direction[i] == "F"):
            for j in range(4):
                shipPos[j] += distance[i] * waypointPos[j]

    northSouth = shipPos[0] - shipPos[2]
    westEast = shipPos[1] - shipPos[3]
    if(northSouth < 0):
        northSouth = northSouth * (-1)
    if(westEast < 0):
        westEast = westEast * (-1)

    return(northSouth+westEast)


puzzle1 = move_ship(directions, distances)
puzzle2 = move_waypoint(directions, distances)
print(puzzle1, puzzle2)