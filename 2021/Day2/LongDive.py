def parse_input():
    data = open("2021/Day2/input2", "r+")
    data = data.read()
    data = data.split("\n")
    
    direction = []
    distance = []
    for entry in data:
        split = entry.split(" ")
        direction.append(split[0])
        distance.append((int)(split[1]))
    return(direction, distance)

def nauticNavigation(direction, distance):
    horiz = 0
    depth = 0
    for i in range(len(direction)):
        if(direction[i] == 'forward'):
            horiz += distance[i]
        elif(direction[i] == 'up'):
            depth -= distance[i]
        else:
            depth += distance[i]
    return (horiz * depth)

def aimingForDepths(direction, distance):
    aim = 0
    horiz = 0
    depth = 0
    for i in range(len(direction)):
        if(direction[i] == 'forward'):
            horiz += distance[i]
            depth += distance[i] * aim
        elif(direction[i] == 'up'):
            aim -= distance[i]
        else:
            aim += distance[i]
    return (horiz * depth)

    

direction, distance = parse_input()
print(nauticNavigation(direction, distance))
print(aimingForDepths(direction, distance))