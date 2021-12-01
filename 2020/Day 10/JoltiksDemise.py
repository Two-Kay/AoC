def convert_to_int(data):
    '''
    Converts input data from String to Integer.
    '''
    output = []
    for i in range(len(data)):
        output.append(int(data[i]))
    return output

data = open("Day 10\input10", "r+")
data = data.read()
data = data.split("\n")
data = convert_to_int(data)

def count_differences(data):
    '''
    Counts how many adapters you need for each jolt.

    Returns the product of the 3 jolt adapters and the 1 jolt adapters.
    '''
    one_jolt=0
    three_jolt=0
    jolts = 0
    for i in range(len(data)):
        smallest_index = -1
        for j in range(len(data)):
            if(data[j] - jolts == 3):
                if(smallest_index == -1):
                    smallest_index = j
            elif(data[j] - jolts == 1):
                smallest_index = j
                break
        if(data[smallest_index] - jolts == 3):
            three_jolt += 1
        elif(data[smallest_index] - jolts == 1):
            one_jolt += 1
        jolts = data[smallest_index]
    three_jolt += 1
    return (one_jolt * three_jolt)

def create_arrangement_tree(data):
    '''
    Builds a pseudo-tree structure of like each possible adapter gosh.
    '''
    tree = []
    jolts = 0
    for i in range(len(data)):
        toCheck = -1
        first_choice = -1
        second_choice = -1
        third_choice = -1
        for j in range(len(data)):
            if(data[j] - jolts == 3):
                third_choice = data[j]
            elif(data[j] - jolts == 2):
                second_choice = data[j]
            elif(data[j] - jolts == 1):
                first_choice = data[j]
            if(data[j] > jolts and toCheck == -1 or data[j] > jolts and toCheck > data[j]):
                toCheck = data[j]
        tree.append([])
        tree[i].append(jolts)
        jolts = toCheck
        if(first_choice != -1):
            tree[i].append(first_choice)
        if(second_choice != -1):
            tree[i].append(second_choice)
        if(third_choice != -1):
            tree[i].append(third_choice)

    add_last = tree[len(tree)-1]
    add_last = add_last[len(add_last)-1]
    tree.append([])
    tree[len(tree)-1].append(add_last)
    tree[len(tree)-1].append(add_last+3)
    
    add_own = tree[len(tree)-1][0] + 3
    tree.append([])
    tree[len(tree)-1].append(add_own)

    return tree

def convert_into_index_tree(tree):
    '''
    Converts the joltage tree into two index lists used for later functions.
    Returns:
    index_list -> A list which simple outputs its *drumroll* index!
    value_index_list -> A list which outputs the index of of the index_list that the value originally points at,
    basically listing the child nodes of each "index node".
    '''
    index_list = []
    value_index_list = []
    for i in range(len(tree)):
        index_list.append(i)
        value_index_list.append([])
        for j in range(len(tree[i])-1):
            value = int(tree[i][j+1])
            for k in range(len(tree)):
                if(tree[k][0] == value):
                    value_index_list[i].append(k)
    value_index_list.pop()
    return (index_list, value_index_list)

def count_paths(index_list, value_index_list):
    '''
    Counts all the possible combinations of adapters you could apply!
    
    It uses an iterative function beginning from the last index
    and overwrites the index values as sum-of-paths values,
    though I suppose a recursive function would be more optimized.
    '''
    i = len(index_list)-1
    index_list[i] = 1
    i -= 1
    while (0 <= i):
        sum = 0
        for j in range(len(value_index_list[i])):
            value_index_list[i][j] = index_list[value_index_list[i][j]]
            sum += value_index_list[i][j]
        index_list[i] = sum
        i -= 1
    return(index_list)

puzzle1 = count_differences(data)
tree = create_arrangement_tree(data)
x, y = convert_into_index_tree(tree)
puzzle_result = count_paths(x, y)
puzzle2 = puzzle_result[0]
print(puzzle1, puzzle2)