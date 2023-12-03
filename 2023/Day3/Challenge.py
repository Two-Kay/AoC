file = "2023/Day3/input"


def is_special(symbol):
    return symbol.isdigit() == False and symbol != "."


def numbery(file):
    output = 0
    matrix = []
    with open(file, "r+") as f:
        for row in f:
            matrix.append(row.strip("\n")[::-1])
    num = 0
    digit = 1
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            marked = False
            if matrix[y][x].isdigit():
                num += digit * int(matrix[y][x])
                digit *= 10
            if (x + 1) >= len(matrix[y]) or matrix[y][x+1].isdigit() == False:
                if x != 0:
                    if is_special(matrix[y][x+1-(len(str(digit)))]):
                        marked = True
                if x < (len(matrix[y]) - 1):
                    if is_special(matrix[y][x+1]):
                        marked = True
                for i in range(len(str(digit)) - 1):
                    if is_special(matrix[y][x+2+i-(len(str(digit)))]):
                        marked = True
                if y != 0:
                    if x != 0:
                        if is_special(matrix[y-1][x+1-(len(str(digit)))]):
                            marked = True
                    if x < (len(matrix[y]) - 1):
                        if is_special(matrix[y-1][x+1]):
                            marked = True
                    for i in range(len(str(digit)) - 1):
                        if is_special(matrix[y-1][x+2+i-(len(str(digit)))]):
                            marked = True
                if y < (len(matrix) - 1):
                    if x != 0:
                        if is_special(matrix[y+1][x+1-(len(str(digit)))]):
                            marked = True
                    if x < (len(matrix[y]) - 1):
                        if is_special(matrix[y+1][x+1]):
                            marked = True
                    for i in range(len(str(digit)) - 1):
                        if is_special(matrix[y+1][x+2+i-(len(str(digit)))]):
                            marked = True
                if marked:
                    output += num
                digit = 1
                num = 0
    return output


def get_number(matrix, y, x):
    num = 0
    digit = 1
    i = x
    while i < len(matrix[y]):
        if matrix[y][i].isdigit() == True:
            i += 1
        else:
            break
    i -= 1
    while i >= 0:
        if matrix[y][i].isdigit() == True:
            num += digit * int(matrix[y][i])
            digit *= 10
        else:
            break
        i -= 1
    return num


def geary(file):
    output = 0
    matrix = []
    with open(file, "r+") as f:
        for row in f:
            matrix.append(row.strip("\n"))
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "*":
                numbers = []
                if y != 0:
                    hasNum = False
                    if x < (len(matrix[y]) - 1):
                        if matrix[y-1][x+1].isdigit():
                            hasNum = True
                            numbers.append(get_number(matrix, y-1, x+1))
                        if matrix[y-1][x].isdigit():
                            if hasNum == False:
                                numbers.append(get_number(matrix, y-1, x))
                                hasNum = True
                        else:
                            hasNum = False
                        if matrix[y-1][x-1].isdigit() and (hasNum == False):
                            numbers.append(get_number(matrix, y-1, x-1))
                if y < len(matrix) - 1:
                    hasNum = False
                    if x < (len(matrix[y]) - 1):
                        if matrix[y+1][x+1].isdigit():
                            hasNum = True
                            numbers.append(get_number(matrix, y+1, x+1))
                        if matrix[y+1][x].isdigit():
                            if hasNum == False:
                                numbers.append(get_number(matrix, y+1, x))
                                hasNum = True
                        else:
                            hasNum = False
                        if matrix[y+1][x-1].isdigit() and (hasNum == False):
                            numbers.append(get_number(matrix, y+1, x-1))
                if x != 0:
                    if matrix[y][x-1].isdigit():
                        numbers.append(get_number(matrix, y, x-1))
                if x < (len(matrix[y]) - 1):
                    if matrix[y][x+1].isdigit():
                        numbers.append(get_number(matrix, y, x+1))
                if len(numbers) == 2:
                    output += numbers[0] * numbers[1]
    return output


print(numbery(file))
print(geary(file))
