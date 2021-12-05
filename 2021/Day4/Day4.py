def convert_to_int(data):
    '''
    Converts input data from String to Integer.
    '''
    output = []
    for i in range(len(data)):
        output.append(int(data[i]))
    return output

data = open("2021\Day4\input", "r+")
data = data.read()
data = data.split("\n")
called = data[0]
called = called.split(",")
called = convert_to_int(called)
bingo = []
start = 2
block = 0
for i in range(len(data)-2):
    if(data[i+2] == ''):
        bingo.append(data[start:(i+2)])
        for j in range(len(bingo[block])):
            entry = bingo[block][j]
            entry = entry.replace("  ", " ")
            if(entry[0] == ' '):
                entry = entry[1:]
            bingo[block][j] = entry.split(" ")
            bingo[block][j] = convert_to_int(bingo[block][j])
        block += 1
        start = i+3

crosses = []
for block in range(len(bingo)):
    crosses.append([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

def squid_Bingo():
    for call in range(len(called)):
        for block in range(len(bingo)):
            amount = [0,0,0,0,0]
            for row in range(len(bingo[block])):
                for column in range (len(bingo[block][row])):
                    if(bingo[block][row][column] == called[call]):
                        crosses[block][row][column] = 1
                    if(crosses[block][row][column] == 1):
                        amount[column] += 1
                if(crosses[block][row] == [1,1,1,1,1]):
                    ret = 0
                    for x in range(len(bingo[block])):
                        for y in range(len(bingo[block][x])):
                            if(crosses[block][x][y] == 0):
                                ret += bingo[block][x][y]
                    return(ret*called[call])
            if(max(amount) == 5):
                ret = 0
                for x in range(len(bingo[block])):
                    for y in range(len(bingo[block][x])):
                        if(crosses[block][x][y] == 0):
                            ret += bingo[block][x][y]
                return(ret*called[call])

def last_Bingo():
    for call in range(len(called)):
        bannedBlocks = []
        for block in range(len(bingo)):
            print(bannedBlocks)
            if(block not in bannedBlocks):
                amount = [0,0,0,0,0]
                for row in range(len(bingo[block])):
                    for column in range (len(bingo[block][row])):
                        if(bingo[block][row][column] == called[call]):
                            crosses[block][row][column] = 1
                        if(crosses[block][row][column] == 1):
                            amount[column] += 1
                    if(crosses[block][row] == [1,1,1,1,1]):
                        if(block not in bannedBlocks):
                            bannedBlocks.append(block)
                        if(len(bannedBlocks) == len(bingo)):
                            ret = 0
                            for x in range(len(bingo[block])):
                                for y in range(len(bingo[block][x])):
                                    if(crosses[block][x][y] == 0):
                                        ret += bingo[block][x][y]
                            return(ret*called[call])
                if(max(amount) == 5):
                    if(block not in bannedBlocks):
                        bannedBlocks.append(block)
                    if(len(bannedBlocks) == len(bingo)):
                        ret = 0
                        for x in range(len(bingo[block])):
                            for y in range(len(bingo[block][x])):
                                if(crosses[block][x][y] == 0):
                                    ret += bingo[block][x][y]
                        return(ret*called[call])




#solution1 = squid_Bingo()
solution2 = last_Bingo()
#print(solution1)
print(solution2)
