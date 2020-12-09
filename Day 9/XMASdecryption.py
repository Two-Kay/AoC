data  = open("Day 9\input9", "r+")
data = data.read()
data = data.split("\n")

def does_it_sum(numbers, current):
    '''
    This function checks whether two different numbers withing the preamble (25 previous numbers)
    sum up to the current number.
    '''
    preamble = numbers[current-25:current]
    for i in range(len(preamble)):
        for j in range(len(preamble)):
            if ((int(preamble[i]) + int(preamble[j]) == int(numbers[current]) and i!=j)):
                return((int(preamble[i]) + int(preamble[j])))
    return 0

def look_for_invalid(data):
    '''
    This function searches for the invalid number, where none of the value-pairs of the preamble sum up to it.
    '''
    i = 25
    while(i < len(data)):
        check = does_it_sum(data, i)
        if(check == 0):
            return data[i]
        i += 1
    return 0

def look_for_set(data, invalid):
    '''
    This function looks for a contiguous set of numbers which all sum up exactly to the invalid number.
    Returns the sum of the minimum and the maximum of the set.
    '''
    for i in range(len(data)):
        sum = 0
        j = i
        check = []
        while(sum < int(invalid)):
            sum += int(data[j])
            check.append(int(data[j]))
            if(sum == int(invalid)):
                return(min(check) + max(check))
            j += 1
    return 0, 0

puzzle1 = look_for_invalid(data)
puzzle2 = look_for_set(data, puzzle1)
print(puzzle1, puzzle2)