data  = open("Day 4\input4.txt", "r+")
data_list = data.read()

def split_entries_up(data=None):
    '''
    Splits the input data up into a two-dimensional list
    which lists down all the passports including a list of all entries.
    '''
    id_list = [[]]
    long_list = data.split("\n")

    longer_list = []
    for i in range(len(long_list)):
        list_line = long_list[i].split(" ")

        for j in range(len(list_line)):
            longer_list.append(list_line[j])

    second_index = 0
    for i in range(len(longer_list)):
        if(longer_list[i]==""):
            id_list.append([])
            second_index += 1
        id_list[second_index].append(longer_list[i])
    return id_list

def validate_passports(data=None):
    '''
    Validates a passport for the correct types of entires (excluding the one you miss).

    Returns the count of all valid passport read from a two-dimensional list.
    '''
    count = 0
    for i in range(len(data)):
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False

        for j in range(len(data[i])):
            entry = data[i][j].split(":")
            if(entry[0] == "byr"):
                byr = True
            elif(entry[0] == "iyr"):
                iyr = True
            elif(entry[0] == "eyr"):
                eyr = True
            elif(entry[0] == "hgt"):
                hgt = True
            elif(entry[0] == "hcl"):
                hcl = True
            elif(entry[0] == "ecl"):
                ecl = True
            elif(entry[0] == "pid"):
                pid = True

        if(byr and iyr and eyr and hgt and hcl and ecl and pid):
            count += 1

    return count

def validate_passport_values(data=None):
    '''
    Validates a passport for the correct types and contents of entires (excluding the one you miss).
    
    Returns the count of all valid passport read from a two-dimensional list.
    '''
    count = 0
    for i in range(len(data)):
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False

        for j in range(len(data[i])):
            entry = data[i][j].split(":")
            if(len(entry)==2):

                if(entry[0] == "byr" and int(entry[1]) >= 1920 and int(entry[1]) <= 2002):
                    byr = True

                elif(entry[0] == "iyr" and int(entry[1]) >= 2010 and int(entry[1]) <= 2020):
                    iyr = True

                elif(entry[0] == "eyr" and int(entry[1]) >= 2020 and int(entry[1]) <= 2030):
                    eyr = True

                elif(entry[0] == "hgt"):
                    value = entry[1]
                    imperial = False
                    metric = False
                    x = value[0]
                    if (x=="0" or x=="1" or x=="2" or x=="3" or x=="4" or x=="5"
                        or x=="6" or x=="7" or x=="8" or x=="9"):
                        for k in range(len(value)-1):
                            if(metric == True):
                                if(value[k+1]=="m"):
                                    metricValue = value[0:3]
                                    isNumber = True
                                    for l in range(3):
                                        if(ord(metricValue[l])>57):
                                            isNumber = False
                                    if(isNumber == True):
                                        if(int(metricValue) >= 150 and int(metricValue) <= 193):
                                            hgt = True
                                    break
                                else:
                                    metric = False
                            elif(imperial == True):
                                if(value[k+1]=="n"):
                                    imperialValue = value[0:2]
                                    isNumber = True
                                    for l in range(2):
                                        if(ord(imperialValue[l])>57):
                                            isNumber = False
                                    if(isNumber == True):
                                        if(int(imperialValue) >= 59 and int(imperialValue) <= 76):
                                            hgt = True
                                    break
                                else:
                                    imperial = False
                            else:
                                if(value[k+1]=="c"):
                                    metric = True
                                elif(value[k+1]=="i"):
                                    imperial = True

                elif(entry[0] == "hcl"):
                    validCount = 0
                    value = entry[1]
                    if(len(value) == 7):
                        if(value[0]=="#"):
                            for k in range(6):
                                x = value[k+1]
                                if(x=="0" or x=="1" or x=="2" or x=="3" or x=="4" or x=="5"
                                or x=="6" or x=="7" or x=="8" or x=="9" or x=="a" or x=="b"
                                or x=="c" or x=="d" or x=="e" or x=="f"):
                                    validCount += 1
                    if(validCount == 6):
                        hcl = True

                elif(entry[0] == "ecl"):
                    x = entry[1]
                    if(x=="amb" or x=="blu" or x=="brn" or x=="gry" or x=="grn" or x=="hzl" or x=="oth"):
                        ecl = True

                elif(entry[0] == "pid"):
                    if(len(entry[1]) == 9):
                        pid = True

        if(byr and iyr and eyr and hgt and hcl and ecl and pid):
            count += 1

    return count

passports = split_entries_up(data_list)
puzzle1 = validate_passports(passports)
puzzle2 = validate_passport_values(passports)
print(puzzle1, puzzle2)