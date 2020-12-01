import pandas as pd
import numpy as np

inputData = pd.read_csv("Day 1\input").to_numpy()

def two_kay(data=None):
    '''
    This function checks through an array to find two numbers
    which add up to 2k20 and returns the product of them.
    '''
    for i in range(len(data)):
        j = i + 1
        while (j < len(data)):
            if ((data[i]+data[j]==2020)):
                return(int(data[i]*data[j]))
            else:
                j = j + 1

def three_kay(data=None):
    '''
    This function checks through an array to find three numbers
    which add up to 2k20 and returns the product of them.
    '''
    for i in range(len(data)):
        j = i + 1
        while (j < len(data)):
            k = j + 1
            while (k < len(data)):
                if ((data[i]+data[j]+data[k]==2020)):
                    return(int(data[i]*data[j]*data[k]))
                else:
                    k = k + 1
            j = j + 1

puzzle1 = two_kay(inputData)
puzzle2 = three_kay(inputData)
print(puzzle1, puzzle2)