data = open("Day 8\input8", "r+")
data = data.read()
data = data.split("\n")

def split_entries_up(data=None):
    '''
    Splits the entires up into 3 categories:
    Operation -> Either acc (accumulator)
                        jmp (jump to index)
                        nop (skip)
    Sign -> Either '+' or '-'
    Value -> The value for each operation
    '''
    operation = []
    sign = []
    value = []

    for i in range(len(data)):
        listy = data[i].split(" ")
        operation.append(listy[0])
        values = listy[1]
        singleSign = values[0]
        singleValue = values[1:len(values)]
        sign.append(singleSign)
        value.append(singleValue)

    return (operation, sign, value)

def execute_code_once(operation, sign, value):
    '''
    Executes the code for as long as it doesn't reach a loop.
    
    Returns the accumulator value on end or once loop is reached.
    '''
    accumulator = 0
    index = 0
    indexList = []
    while(index < len(operation)):
        for i in range(len(indexList)):
            if(index == indexList[i]):
                return accumulator
        indexList.append(index)
        if(operation[index] == "acc"):
            if(sign[index] == "+"):
                accumulator += int(value[index])
                index += 1
            elif(sign[index] == "-"):
                accumulator -= int(value[index])
                index += 1
        elif(operation[index] == "jmp"):
            if(sign[index] == "+"):
                index += int(value[index])
            elif(sign[index] == "-"):
                index -= int(value[index])
        else:
            index += 1
    return accumulator

def figure_out_a_fixy_solution(operation, sign, value):
    '''
    Figures out what 'jmp' or 'nop' operation needs to be changed
    in order to get the code to end.

    Returns index of operator that needs to be changed.
    '''
    accumulator = 0
    index = 0
    indexList = []
    repetition = 0
    repeat = 0
    indexToChange = 0
    while(index < len(operation)):
        for i in range(len(indexList)):
            if(index == indexList[i]):
                repetition += 1
                repeat = 0
                for j in range(len(indexList)):
                    indexList.pop()
                index = 0
                break
        indexList.append(index)
        if(operation[index] == "acc"):
            if(sign[index] == "+"):
                accumulator += int(value[index])
                index += 1
            elif(sign[index] == "-"):
                accumulator -= int(value[index])
                index += 1
        if(repetition == 0):
            if(operation[index] == "jmp"):
                if(sign[index] == "+"):
                    index += int(value[index])
                elif(sign[index] == "-"):
                    index -= int(value[index])
            elif(operation[index] == "nop"):
                    index += 1
        else:
            if(operation[index] == "jmp"):
                if(repeat != repetition-1):
                    if(sign[index] == "+"):
                        index += int(value[index])
                    elif(sign[index] == "-"):
                        index -= int(value[index])
                    repeat += 1
                else:
                    indexToChange = index
                    index +=1
                    repeat +=1
            elif(operation[index] == "nop"):
                if(repeat == repetition -1):
                    indexToChange = index
                    if(sign[index] == "+"):
                        index += int(value[index])
                    elif(sign[index] == "-"):
                        index -= int(value[index])
                else:
                    index +=1
                    repeat +=1
    return indexToChange

def run_correctly(operation, sign, value):
    '''
    If one defuctional 'jmp' or 'nop' exists, the code will fix it by switching 'jmp' to 'nop' or reverse.

    Returns the accumulator as if the code was running properly.
    '''
    accumulator = 0
    index = 0
    indexToChange = figure_out_a_fixy_solution(operation, sign, value)
    while(index < len(operation)):
        if(operation[index] == "acc"):
            if(sign[index] == "+"):
                accumulator += int(value[index])
                index += 1
            elif(sign[index] == "-"):
                accumulator -= int(value[index])
                index += 1
        elif(operation[index] == "jmp"):
            if(indexToChange != index):
                if(sign[index] == "+"):
                    index += int(value[index])
                elif(sign[index] == "-"):
                    index -= int(value[index])
            else:
                index +=1
        else:
            if(indexToChange == index):
                if(sign[index] == "+"):
                    index += int(value[index])
                elif(sign[index] == "-"):
                    index -= int(value[index])
            else:
                index +=1
    return accumulator

operation, sign, value = split_entries_up(data)
puzzle1 = (execute_code_once(operation, sign, value))
puzzle2 = (run_correctly(operation, sign, value))
print(puzzle1, puzzle2)