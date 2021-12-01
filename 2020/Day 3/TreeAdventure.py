import numpy as np
import pandas as pd

data = pd.read_csv("Day 3\input3").to_numpy()

def clean_input(data=None):
    '''
    Cleans input data because pandas and numpy include the "['']" into the string...
    '''
    cleaned = []
    for i in range(len(data)):
        content = str(data[i])
        cleaned.append(content[2:(len(content)-2)])
    return cleaned

def tree_adventure(map=None, x_increment=None, y_increment=None):
    '''
    You go on a tree adventure at the airport!
    The increments define how many steps you take on each axis of the airport map.
    '''
    tree = 0
    x_cord = 0
    y_cord = y_increment
    while(y_cord < len(map)):
        x_cord = x_cord + x_increment
        slope = str(map[y_cord])
        if(x_cord >= len(slope)):
            x_cord = x_cord - len(slope)
        if(ord(slope[x_cord]) == 35):
            tree = tree + 1
        y_cord = y_cord + y_increment
    return (tree)

def many_adventures(map=None):
    '''
    You try to go on many adventures and multiply the results you obtain!
    '''
    treees =  tree_adventure(map, 1, 1) * tree_adventure(map, 3, 1) * tree_adventure(map, 5, 1) * tree_adventure(map, 7, 1) * tree_adventure(map, 1, 2)
    return treees

map = clean_input(data)
puzzle1 = tree_adventure(map, 3, 1)
puzzle2 = many_adventures(map)
print(puzzle1, puzzle2)