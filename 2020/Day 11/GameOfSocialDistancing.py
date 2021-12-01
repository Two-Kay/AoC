def convert_to_list(data):
    '''
    Converts a string to a list of strings.
    '''
    entirity = []
    for i in range(len(data)):
        output = []
        row = data[i]
        for j in range(len(row)):
            output.append(row[j])
        entirity.append(output)
    return entirity

data = open("Day 11\input11", "r+")
data = data.read()
data = data.split("\n")
data = convert_to_list(data)

def fill_seats(data):
    '''
    Plays minesweeper and leaves the seat if 4 occupied seats are adjacent.
    '''
    still_simulating = True
    while(still_simulating == True):
        still_simulating = False
        #print("Iteration start")
        for i in range(len(data)):
            row = data[i]
            occupied = 0
            for j in range(len(row)):
                if(row[j] == "L"):
                    if(j == 0):
                        if(row[j+1] != "#" and row[j+1] != "1"):
                            if(i == len(data) - 1):
                                above = data[i-1]
                                if(above[j] != "#" and above[j+1] != "#"
                                and above[j] != "1" and above[j+1] != "1"):
                                    row[j] = "0"
                                    still_simulating = True
                            elif(i == 0):
                                below = data[i+1]
                                if(below[j] != "#" and below[j+1] != "#"
                                and below[j] != "1" and below[j+1] != "1"):
                                    row[j] = "0"
                                    still_simulating = True
                            else:
                                above = data[i-1]
                                below = data[i+1]
                                if(below[j] != "#" and below[j+1] != "#"
                                and below[j] != "1" and below[j+1] != "1"
                                and above[j] != "#" and above[j+1] != "#"
                                and above[j] != "1" and above[j+1] != "1"):
                                    row[j] = "0"
                                    still_simulating = True
                    elif(j == len(row) - 1):
                        if(row[j-1] != "#" and row[j-1] != "1"):
                            if(i == len(data) - 1):
                                above = data[i-1]
                                if(above[j] != "#" and above[j-1] != "#"
                                and above[j] != "1" and above[j-1] != "1"):
                                    row[j] = "0"
                                    still_simulating = True
                            elif(i == 0):
                                below = data[i+1]
                                if(below[j] != "#" and below[j-1] != "#"
                                and below[j] != "1" and below[j-1] != "1"):
                                    row[j] = "0"
                                    still_simulating = True
                            else:
                                above = data[i-1]
                                below = data[i+1]
                                if(below[j] != "#" and below[j-1] != "#"
                                and below[j] != "1" and below[j-1] != "1"
                                and above[j] != "#" and above[j-1] != "#"
                                and above[j] != "1" and above[j-1] != "1"):
                                    row[j] = "0"
                                    still_simulating = True
                    else:
                        if(row[j-1] != "#" and row[j+1] != "#"
                        and row[j-1] != "1" and row[j+1] != "1"):
                            if(i == len(data) - 1):
                                above = data[i-1]
                                if(above[j] != "#" and above[j-1] != "#" and above[j+1] != "#"
                                and above[j] != "1" and above[j-1] != "1" and above[j+1] != "1"):
                                    row[j] = "0"
                                    still_simulating = True
                            elif(i == 0):
                                below = data[i+1]
                                if(below[j] != "#" and below[j-1] != "#" and below[j+1] != "#"
                                and below[j] != "1" and below[j-1] != "1" and below[j+1] != "1"):
                                    row[j] = "0"
                                    still_simulating = True
                            else:
                                above = data[i-1]
                                below = data[i+1]
                                if(below[j] != "#" and below[j-1] != "#" and below[j+1] != "#"
                                and below[j] != "1" and below[j-1] != "1" and below[j+1] != "1"
                                and above[j] != "#" and above[j-1] != "#" and above[j+1] != "#"
                                and above[j] != "1" and above[j-1] != "1" and above[j+1] != "1"):
                                    row[j] = "0"
                                    still_simulating = True
                elif(row[j] == "#"):
                    occupied = 0
                    if(j == 0):
                        if(row[j+1] == "#" or row[j+1] == "1"):
                            occupied += 1
                        if(i == len(data) - 1):
                            above = data[i-1]
                            if(above[j] == "#" or above[j] == "1"):
                                occupied +=1
                            if(above[j+1] == "#" or above[j+1] == "1"):
                                occupied +=1
                        elif(i == 0):
                            below = data[i+1]
                            if(below[j] == "#" or below[j] == "1"):
                                occupied +=1
                            if(below[j+1] == "#" or below[j+1] == "1"):
                                occupied +=1
                        else:
                            above = data[i-1]
                            below = data[i+1]
                            if(above[j] == "#" or above[j] == "1"):
                                occupied +=1
                            if(above[j+1] == "#" or above[j+1] == "1"):
                                occupied +=1
                            if(below[j] == "#" or below[j] == "1"):
                                occupied +=1
                            if(below[j+1] == "#" or below[j+1] == "1"):
                                occupied +=1
                    elif(j == len(row) - 1):
                        if(row[j-1] == "#" or row[j-1] == "1"):
                            occupied += 1
                        if(i == len(data) - 1):
                            above = data[i-1]
                            if(above[j] == "#" or above[j] == "1"):
                                occupied +=1
                            if(above[j-1] == "#" or above[j-1] == "1"):
                                occupied +=1
                        elif(i == 0):
                            below = data[i+1]
                            if(below[j] == "#" or below[j] == "1"):
                                occupied +=1
                            if(below[j-1] == "#" or below[j-1] == "1"):
                                occupied +=1
                        else:
                            above = data[i-1]
                            below = data[i+1]
                            if(above[j] == "#" or above[j] == "1"):
                                occupied +=1
                            if(above[j-1] == "#" or above[j-1] == "1"):
                                occupied +=1
                            if(below[j] == "#" or below[j] == "1"):
                                occupied +=1
                            if(below[j-1] == "#" or below[j-1] == "1"):
                                occupied +=1
                    else:
                        if(row[j+1] == "#" or row[j+1] == "1"):
                            occupied += 1
                        if(row[j-1] == "#" or row[j-1] == "1"):
                            occupied += 1
                        if(i == len(data) - 1):
                            above = data[i-1]
                            if(above[j] == "#" or above[j] == "1"):
                                occupied +=1
                            if(above[j-1] == "#" or above[j-1] == "1"):
                                occupied +=1
                            if(above[j+1] == "#" or above[j+1] == "1"):
                                occupied +=1
                        elif(i == 0):
                            below = data[i+1]
                            if(below[j] == "#" or below[j] == "1"):
                                occupied +=1
                            if(below[j-1] == "#" or below[j-1] == "1"):
                                occupied +=1
                            if(below[j+1] == "#" or below[j+1] == "1"):
                                occupied +=1
                        else:
                            above = data[i-1]
                            below = data[i+1]
                            if(above[j] == "#" or above[j] == "1"):
                                occupied +=1
                            if(above[j-1] == "#" or above[j-1] == "1"):
                                occupied +=1
                            if(below[j] == "#" or below[j] == "1"):
                                occupied +=1
                            if(below[j-1] == "#" or below[j-1] == "1"):
                                occupied +=1
                            if(below[j+1] == "#" or below[j+1] == "1"):
                                occupied +=1
                            if(above[j+1] == "#" or above[j+1] == "1"):
                                occupied +=1
                    if(occupied >= 4):
                        row[j] = "1"
                        still_simulating = True
            #print(i, row)
            data[i] = row
        for x in range(len(data)):
            row = data[x]
            for y in range(len(row)):
                if(row[y] == "0"):
                    row[y] = "#"
                elif(row[y] == "1"):
                    row[y] = "L"
            data[x] = row
    return data

def social_distancing(data):
    '''
    Plays minesweeper^2 leaves the seat if at least 5 of the first seats of each direction (diagonals included) are occupied seats.
    '''
    still_simulating = True
    while(still_simulating == True):
        still_simulating = False
        for i in range(len(data)):
            row = data[i]
            occupied = 0
            for j in range(len(row)):
                if(row[j] == "L"):
                    occupied = 0
                    iteration = j - 1
                    while(iteration >= 0):
                        if(row[iteration] == "#" or row[iteration] == "1"):
                            occupied +=1
                            break
                        if(row[iteration] == "L" or row[iteration] == "0"):
                            break
                        iteration -=1
                    iteration = j + 1
                    while(iteration < len(row)):
                        if(row[iteration] == "#" or row[iteration] == "1"):
                            occupied +=1
                            break
                        if(row[iteration] == "L" or row[iteration] == "0"):
                            break
                        iteration +=1
                    iterationI = i - 1
                    iterationJ = j - 1
                    while(iterationJ >= 0 and iterationI >= 0):
                        if(data[iterationI][iterationJ] == "#"
                        or data[iterationI][iterationJ] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][iterationJ] == "L"
                        or data[iterationI][iterationJ] == "0"):
                            break
                        iterationI -=1
                        iterationJ -=1
                    iterationI = i - 1
                    while(iterationI >= 0):
                        if(data[iterationI][j] == "#"
                        or data[iterationI][j] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][j] == "L"
                        or data[iterationI][j] == "0"):
                            break
                        iterationI -=1
                    iterationI = i - 1
                    iterationJ = j + 1
                    while(iterationJ < len(row) and iterationI >= 0):
                        if(data[iterationI][iterationJ] == "#"
                        or data[iterationI][iterationJ] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][iterationJ] == "L"
                        or data[iterationI][iterationJ] == "0"):
                            break
                        iterationI -=1
                        iterationJ +=1
                    iterationI = i + 1
                    iterationJ = j - 1
                    while(iterationJ >= 0 and iterationI < len(data)):
                        if(data[iterationI][iterationJ] == "#"
                        or data[iterationI][iterationJ] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][iterationJ] == "L"
                        or data[iterationI][iterationJ] == "0"):
                            break
                        iterationI +=1
                        iterationJ -=1
                    iterationI = i + 1
                    while(iterationI < len(data)):
                        if(data[iterationI][j] == "#"
                        or data[iterationI][j] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][j] == "L"
                        or data[iterationI][j] == "0"):
                            break
                        iterationI +=1
                    iterationI = i + 1
                    iterationJ = j + 1
                    while(iterationJ < len(row) and iterationI < len(data)):
                        if(data[iterationI][iterationJ] == "#"
                        or data[iterationI][iterationJ] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][iterationJ] == "L"
                        or data[iterationI][iterationJ] == "0"):
                            break
                        iterationI +=1
                        iterationJ +=1
                    if(occupied == 0):
                        row[j] = "0"
                        still_simulating = True

                elif(row[j] == "#"):
                    occupied = 0
                    iteration = j - 1
                    while(iteration >= 0):
                        if(row[iteration] == "#" or row[iteration] == "1"):
                            occupied +=1
                            break
                        if(row[iteration] == "L" or row[iteration] == "0"):
                            break
                        iteration -=1
                    iteration = j + 1
                    while(iteration < len(row)):
                        if(row[iteration] == "#" or row[iteration] == "1"):
                            occupied +=1
                            break
                        if(row[iteration] == "L" or row[iteration] == "0"):
                            break
                        iteration +=1
                    iterationI = i - 1
                    iterationJ = j - 1
                    while(iterationJ >= 0 and iterationI >= 0):
                        if(data[iterationI][iterationJ] == "#"
                        or data[iterationI][iterationJ] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][iterationJ] == "L"
                        or data[iterationI][iterationJ] == "0"):
                            break
                        iterationI -=1
                        iterationJ -=1
                    iterationI = i - 1
                    while(iterationI >= 0):
                        if(data[iterationI][j] == "#"
                        or data[iterationI][j] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][j] == "L"
                        or data[iterationI][j] == "0"):
                            break
                        iterationI -=1
                    iterationI = i - 1
                    iterationJ = j + 1
                    while(iterationJ < len(row) and iterationI >= 0):
                        if(data[iterationI][iterationJ] == "#"
                        or data[iterationI][iterationJ] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][iterationJ] == "L"
                        or data[iterationI][iterationJ] == "0"):
                            break
                        iterationI -=1
                        iterationJ +=1
                    iterationI = i + 1
                    iterationJ = j - 1
                    while(iterationJ >= 0 and iterationI < len(data)):
                        if(data[iterationI][iterationJ] == "#"
                        or data[iterationI][iterationJ] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][iterationJ] == "L"
                        or data[iterationI][iterationJ] == "0"):
                            break
                        iterationI +=1
                        iterationJ -=1
                    iterationI = i + 1
                    while(iterationI < len(data)):
                        if(data[iterationI][j] == "#"
                        or data[iterationI][j] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][j] == "L"
                        or data[iterationI][j] == "0"):
                            break
                        iterationI +=1
                    iterationI = i + 1
                    iterationJ = j + 1
                    while(iterationJ < len(row) and iterationI < len(data)):
                        if(data[iterationI][iterationJ] == "#"
                        or data[iterationI][iterationJ] == "1"):
                            occupied +=1
                            break
                        if(data[iterationI][iterationJ] == "L"
                        or data[iterationI][iterationJ] == "0"):
                            break
                        iterationI +=1
                        iterationJ +=1
                    if(occupied >= 5):
                        row[j] = "1"
                        still_simulating = True
            #print(i, row)
            data[i] = row

        for x in range(len(data)):
            row = data[x]
            for y in range(len(row)):
                if(row[y] == "0"):
                    row[y] = "#"
                elif(row[y] == "1"):
                    row[y] = "L"
            data[x] = row
    return data

def count_occupied_seats(data):
    '''
    counts all the occupied seats
    '''
    count = 0
    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
            if (row[j] == "#"):
                count += 1
    return count

seats = fill_seats(data)
puzzle1 = count_occupied_seats(seats)

data = open("Day 11\input11", "r+")
data = data.read()
data = data.split("\n")
data = convert_to_list(data)

seats = social_distancing(data)
puzzle2 = count_occupied_seats(seats)
print(puzzle1, puzzle2)