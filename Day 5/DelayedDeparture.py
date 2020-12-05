data = open("Day 5\input5", "r+")
data = data.read()
data = data.split("\n")

def split_entries_up(data=None):
    '''
    Splits entries up into rows and columns where
    the first 7 characters are the rows and the last 3 the columns.
    '''
    rows = []
    columns = []
    for i in range(len(data)):
        value = data[i]
        rows.append(value[0:7])
        columns.append(value[7:11])
    return (rows, columns)

def find_seat_ID(row, column):
    '''
    This function tells you the ID of your seat!

    Input: Binary space partitioning code for row and column.

    Output: ID of seat.
    '''

    upperRow = 127
    lowerRow = 0
    upperColumn = 7
    lowerColumn = 0
    returnRow = 0
    returnColumn = 0

    for i in range(len(row)-1):
        if(row[i] == "F"):
            upperRow = int(upperRow - ((upperRow-lowerRow)/2))
        elif(row[i] == "B"):
            lowerRow = int(lowerRow + ((upperRow-lowerRow)/2))+1

    if(row[len(row)-1]=="B"):
        returnRow = upperRow
    else:
        returnRow = lowerRow

    for j in range(len(column)-1):
        if(column[j] == "L"):
            upperColumn = int(upperColumn - ((upperColumn-lowerColumn)/2))
        elif(column[j] == "R"):
            lowerColumn = int(lowerColumn + ((upperColumn-lowerColumn)/2))+1

    if(column[len(column)-1]=="R"):
        returnColumn = upperColumn
    else:
        returnColumn = lowerColumn

    return((returnRow*8)+returnColumn)

def find_seat(row, column):
    '''
    This function tells you what position your seat is at!

    Input: Binary space partitioning code for row and column.

    Output: Index of row and column.
    '''

    upperRow = 127
    lowerRow = 0
    upperColumn = 7
    lowerColumn = 0
    returnRow = 0
    returnColumn = 0

    for i in range(len(row)-1):
        if(row[i] == "F"):
            upperRow = int(upperRow - ((upperRow-lowerRow)/2))
        elif(row[i] == "B"):
            lowerRow = int(lowerRow + ((upperRow-lowerRow)/2))+1

    if(row[len(row)-1]=="B"):
        returnRow = upperRow
    else:
        returnRow = lowerRow

    for j in range(len(column)-1):
        if(column[j] == "L"):
            upperColumn = int(upperColumn - ((upperColumn-lowerColumn)/2))
        elif(column[j] == "R"):
            lowerColumn = int(lowerColumn + ((upperColumn-lowerColumn)/2))+1

    if(column[len(column)-1]=="R"):
        returnColumn = upperColumn
    else:
        returnColumn = lowerColumn

    return(returnRow, returnColumn)

def check_for_highest_ID(rows, columns):
    '''
    This function checks for the highest ID it can find!

    Input: Binary space partitioning code for a list of rows and columns.

    Output: The highest ID.
    '''

    id = 0
    for i in range(len(rows)):
        row = rows[i]
        column = columns[i]
        toCheck = find_seat_ID(row, column)
        if(toCheck>id):
            id = toCheck
    return id

def fillPlane(rows, columns):
    '''
    This function fills a plane up where a "#" represents an occupied seat
    and a "0" an unoccupied seat!

    Input: Binary space partitioning code for a list of rows and columns.

    Output: Two dimensional list of all seats assuming plane has 128 rows.
    '''

    seats = [["0","0","0","0","0","0","0","0"]]
    for j in range(128):
        seats.append(["0","0","0","0","0","0","0","0"])

    for i in range(len(rows)):
        row = rows[i]
        column = columns[i]
        row, column = find_seat(row, column)
        seats[row][column] = "#"
    return seats

def search_for_missing_ID(plane):
    '''
    This function searches for the missing seat in the plane, so you can finally depart!

    Input: Two dimensional list of the seating of the plane.

    Output: Seat ID of the missing seat.
    '''

    search = 0
    for i in range(len(plane)):
        if(plane[i][0] == "#"):
            search = i
            break

    while(search < len(plane)):
        for j in range(len(plane[search])):
            if(plane[search][j] == "0"):
                row = search
                column = j
                return((row*8)+column)
        search += 1
    return False

rows, columns = split_entries_up(data)
puzzle1 = check_for_highest_ID(rows, columns)
plane = fillPlane(rows, columns)
puzzle2 = search_for_missing_ID(plane)
print(puzzle1, puzzle2)