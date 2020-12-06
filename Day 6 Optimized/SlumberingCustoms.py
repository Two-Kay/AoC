import collections

data = open("Day 6\input6", "r+")
data = data.read()
data = data.split("\n")

def split_entries_up(data=None):
    '''
    Splits all answers into groups as a two dimensional list!
    '''

    answers = [[]]
    entry = 0
    group = 0
    while(entry < len(data)):
        if(data[entry]==""):
            group += 1
            entry += 1
            answers.append([])
            answers[group].append(data[entry])
        else:
            answers[group].append(data[entry])
        entry+=1
    return answers

def add_two_lists(listA = None, listB = None):
    '''
    Adds the value of the listB to listA for each entry, must be of the same length.

    Returns a single list.
    '''

    if(len(listA) != len(listB)):
        print("Lists aren't of the same length! First list will be returned as it was...")
    else:
        for i in range(len(listA)):
            listA[i] += listB[i]
    return listA

def check_two_lists(listA = None, listB = None):
    '''
    Checks if the value between two entries in listA and listB correlate,
    if so the value of listA remains the same, otherwise it turns to 0.

    Returns a single list.
    '''

    if(len(listA) != len(listB)):
        print("Lists aren't of the same length! First list will be returned as it was...")
    else:
        for i in range(len(listA)):
            if(listA[i] != listB[i]):
                listA[i] = 0
    return listA

def alphabet_sum(input=None):
    '''
    Counts all the entries of a list which are 1 or higher.
    '''

    sum = 0
    for i in range(len(input)):
        if(input[i] > 0):
            sum += 1
    return sum

def count_group_ortimized(group=None):
    '''
    Twokay's more optimized variant of the first puzzle.

    Returns the sum for each letter that has occured within in a group
    (not the total numbers of letters).
    '''

    occurrences = 0
    for word in range(len(group)):
        answers = collections.Counter(group[word])

        if(occurrences == 0):
            listy = []
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                listy.append(answers[letter])
            occurrences = listy

        else:
            listy = []
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                listy.append(answers[letter])
            occurrences = add_two_lists(occurrences, listy)

    return(alphabet_sum(input=occurrences))

def count_group_andtimized(group=None):
    '''
    Twokay's more optimized variant of the first puzzle.

    Returns the sum for each letter that has occured for all members in a group
    (not the total numbers of letters).
    '''

    occurrences = 0
    for word in range(len(group)):
        answers = collections.Counter(group[word])

        if(occurrences == 0):
            listy = []
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                listy.append(answers[letter])
            occurrences = listy

        else:
            listy = []
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                listy.append(answers[letter])
            occurrences = check_two_lists(occurrences, listy)

    return(alphabet_sum(input=occurrences))

def check_everyone(data=None):
    '''
    Checks the two functions above on all groups.
    '''
    sumOr = 0
    sumAnd = 0
    for i in range(len(data)):
        sumOr += count_group_ortimized(group=data[i])
        sumAnd += count_group_andtimized(data[i])
    return (sumOr, sumAnd)

groups_data = split_entries_up(data)
puzzle1, puzzle2 = check_everyone(groups_data)
print(puzzle1,puzzle2)