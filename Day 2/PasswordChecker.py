import numpy as np
import pandas as pd

data = pd.read_csv("Day 2\input2").to_numpy()

def divide_input_data(input=None):
    '''
    Parses the input data into desired snippets
    only containing the relevant values to validate a password!

    Returns:
    startingRange -> A list element which contains the first index/number for each password.
    endingRange -> A list element which contains the last index/number for each password.
    character -> The character that's being checked with the password.
    password -> The password the user wants to check.
    '''
    startingRange = []
    endingRange = []
    character = []
    password = []

    for i in range((len(input))):


        entry = str(input[i])

        rangeBoundary = -1
        firstBoundary = -1
        secondBoundary = -1

        for j in range(len(entry)):
            if (ord(entry[j])==32):
                if(firstBoundary == -1):
                    firstBoundary = j
                else:
                    secondBoundary = j
                    break
            elif (ord(entry[j])==45):
                rangeBoundy = j

        startingRange.append(entry[2:rangeBoundy])
        endingRange.append(entry[(rangeBoundy+1):firstBoundary])
        character.append(entry[(firstBoundary+1):(secondBoundary-1)])
        password.append(entry[(secondBoundary+1):(len(entry)-2)])
    return (startingRange, endingRange, character, password)

def count_valid_passwords(startingRange=None, endingRange=None,
                          character=None, password=None):
    '''
    Counts all valid passwords where the count of the character is within the range of startingRange and endingRange.
    '''
    validCount = 0

    for i in range(len(password)):
        count = 0
        currentPassword = password[i]

        for j in range(len(currentPassword)):
            if(currentPassword[j]==character[i]):
                count = count + 1
        
        if(count >= int(startingRange[i]) and count <= int(endingRange[i])):
            validCount = validCount + 1
    return validCount

def newPolicy_count_valid_passwords(firstIndex=None, secondIndex=None,
                                    character=None, password=None):
    '''
    Counts all valid passwords where the first index and the second index (counting from 1)
    of the password contain the character at least and at most one time.
    '''
    validCount = 0

    for i in range(len(password)):
        count = 0
        currentPassword = password[i]

        for j in range(len(currentPassword)):
            if(currentPassword[j]==character[i]):
                count = count + 1
        
        if((character[i] == currentPassword[int(firstIndex[i])-1])
           != (character[i] == currentPassword[int(secondIndex[i])-1])):
          
            validCount = validCount + 1
    return validCount

startingRange, endingRange, character, password = divide_input_data(input=data)
puzzle1 = count_valid_passwords(startingRange,endingRange,character,password)
puzzle2 = newPolicy_count_valid_passwords(startingRange,endingRange,character,password)
print(puzzle1, puzzle2)