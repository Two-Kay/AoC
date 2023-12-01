data = open("2023/Day1/input", "r+")
data = data.read()
data = data.split("\n")


def numbers_add(data=None):
    sum = 0
    for row in data:
        num = 0
        for i in range(len(row)):
            try:
                num += 10 * int(row[i])
                break
            except:
                continue
        for i in range(len(row)):
            try:
                num += int(row[len(row)-1-i])
                break
            except:
                continue
        sum += num
    return sum


def calibrated(data=None):
    numbers = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]
    sum = 0
    for row in data:
        num = 0
        i = 0
        while i < len(row):
            try:
                num += 10 * int(row[i])
                i = len(row)
            except:
                for number in numbers:
                    if number in row[:i+1]:
                        num += 10 * numbers.index(number)
                        i = len(row)
                        break
            i += 1
        i = 0
        while i < len(row):
            try:
                num += int(row[len(row)-1-i])
                i = len(row)
            except:
                for number in numbers:
                    if number in row[len(row)-1-i:]:
                        num += numbers.index(number)
                        i = len(row)
                        break
            i += 1
        sum += num
    return sum


print(numbers_add(data))
print(calibrated(data))
