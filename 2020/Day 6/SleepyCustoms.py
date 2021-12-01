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

def count_group_or(group=None):
    '''
    How not to do it:

    Count up all the occurances one-by-one (because someone underestimated the task)

    Returns the sum for each letter that has occured within in a group
    (not the total numbers of letters).
    '''
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0

    for firstIteration in range(len(group)):
        answers = group[firstIteration]

        for secondIteration in range(len(answers)):

            if(answers[secondIteration]=="a"):
                a = 1
            elif(answers[secondIteration]=="b"):
                b = 1
            elif(answers[secondIteration]=="c"):
                c = 1
            elif(answers[secondIteration]=="d"):
                d = 1
            elif(answers[secondIteration]=="e"):
                e = 1
            elif(answers[secondIteration]=="f"):
                f = 1
            elif(answers[secondIteration]=="g"):
                g = 1
            elif(answers[secondIteration]=="h"):
                h = 1
            elif(answers[secondIteration]=="i"):
                i = 1
            elif(answers[secondIteration]=="j"):
                j = 1
            elif(answers[secondIteration]=="k"):
                k = 1
            elif(answers[secondIteration]=="l"):
                l = 1
            elif(answers[secondIteration]=="m"):
                m = 1
            elif(answers[secondIteration]=="n"):
                n = 1
            elif(answers[secondIteration]=="o"):
                o = 1
            elif(answers[secondIteration]=="p"):
                p = 1
            elif(answers[secondIteration]=="q"):
                q = 1
            elif(answers[secondIteration]=="r"):
                r = 1
            elif(answers[secondIteration]=="s"):
                s = 1
            elif(answers[secondIteration]=="t"):
                t = 1
            elif(answers[secondIteration]=="u"):
                u = 1
            elif(answers[secondIteration]=="v"):
                v = 1
            elif(answers[secondIteration]=="w"):
                w = 1
            elif(answers[secondIteration]=="x"):
                x = 1
            elif(answers[secondIteration]=="y"):
                y = 1
            elif(answers[secondIteration]=="z"):
                z = 1

    return(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z)

def count_group_and(group=None):
    '''
    How not to do it:

    Count up all the occurances one-by-one (because someone underestimated the task)

    Returns the sum for each letter that has occured for all members in a group
    (not the total numbers of letters).
    '''
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0

    for firstIteration in range(len(group)):
        answers = group[firstIteration]

        hasA = False
        hasB = False
        hasC = False
        hasD = False
        hasE = False
        hasF = False
        hasG = False
        hasH = False
        hasI = False
        hasJ = False
        hasK = False
        hasL = False
        hasM = False
        hasN = False
        hasO = False
        hasP = False
        hasQ = False
        hasR = False
        hasS = False
        hasT = False
        hasU = False
        hasV = False
        hasW = False
        hasX = False
        hasY = False
        hasZ = False
        
        for secondIteration in range(len(answers)):
            if(answers[secondIteration]=="a" and hasA == False):
                a += 1
            elif(answers[secondIteration]=="b" and hasB == False):
                b += 1
            elif(answers[secondIteration]=="c" and hasC == False):
                c += 1
            elif(answers[secondIteration]=="d" and hasD == False):
                d += 1
            elif(answers[secondIteration]=="e" and hasE == False):
                e += 1
            elif(answers[secondIteration]=="f" and hasF == False):
                f += 1
            elif(answers[secondIteration]=="g" and hasG == False):
                g += 1
            elif(answers[secondIteration]=="h" and hasH == False):
                h += 1
            elif(answers[secondIteration]=="i" and hasI == False):
                i += 1
            elif(answers[secondIteration]=="j" and hasJ == False):
                j += 1
            elif(answers[secondIteration]=="k" and hasK == False):
                k += 1
            elif(answers[secondIteration]=="l" and hasL == False):
                l += 1
            elif(answers[secondIteration]=="m" and hasM == False):
                m += 1
            elif(answers[secondIteration]=="n" and hasN == False):
                n += 1
            elif(answers[secondIteration]=="o" and hasO == False):
                o += 1
            elif(answers[secondIteration]=="p" and hasP == False):
                p += 1
            elif(answers[secondIteration]=="q" and hasQ == False):
                q += 1
            elif(answers[secondIteration]=="r" and hasR == False):
                r += 1
            elif(answers[secondIteration]=="s" and hasS == False):
                s += 1
            elif(answers[secondIteration]=="t" and hasT == False):
                t += 1
            elif(answers[secondIteration]=="u" and hasU == False):
                u += 1
            elif(answers[secondIteration]=="v" and hasV == False):
                v += 1
            elif(answers[secondIteration]=="w" and hasW == False):
                w += 1
            elif(answers[secondIteration]=="x" and hasX == False):
                x += 1
            elif(answers[secondIteration]=="y" and hasY == False):
                y += 1
            elif(answers[secondIteration]=="z" and hasZ == False):
                z += 1

    if(a == len(group)):
        a = 1
    else:
        a = 0
    if(b == len(group)):
        b = 1
    else:
        b = 0
    if(c == len(group)):
        c = 1
    else:
        c = 0
    if(d == len(group)):
        d = 1
    else:
        d = 0
    if(e == len(group)):
        e = 1
    else:
        e = 0
    if(f == len(group)):
        f = 1
    else:
        f = 0
    if(g == len(group)):
        g = 1
    else:
        g = 0
    if(h == len(group)):
        h = 1
    else:
        h = 0
    if(i == len(group)):
        i = 1
    else:
        i = 0
    if(j == len(group)):
        j = 1
    else:
        j = 0
    if(k == len(group)):
        k = 1
    else:
        k = 0
    if(l == len(group)):
        l = 1
    else:
        l = 0
    if(m == len(group)):
        m = 1
    else:
        m = 0
    if(n == len(group)):
        n = 1
    else:
        n = 0
    if(o == len(group)):
        o = 1
    else:
        o = 0
    if(p == len(group)):
        p = 1
    else:
        p = 0
    if(q == len(group)):
        q = 1
    else:
        q = 0
    if(r == len(group)):
        r = 1
    else:
        r = 0
    if(s == len(group)):
        s = 1
    else:
        s = 0
    if(t == len(group)):
        t = 1
    else:
        t = 0
    if(u == len(group)):
        u = 1
    else:
        u = 0
    if(v == len(group)):
        v = 1
    else:
        v = 0
    if(w == len(group)):
        w = 1
    else:
        w = 0
    if(x == len(group)):
        x = 1
    else:
        x = 0
    if(y == len(group)):
        y = 1
    else:
        y = 0
    if(z == len(group)):
        z = 1
    else:
        z = 0
    
    return(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z)

def check_everyone(data=None):
    '''
    Checks the two functions above on all groups.
    '''
    sumOr = 0
    sumAnd = 0
    for i in range(len(data)):
        sumOr += count_group_or(data[i])
        sumAnd += count_group_and(data[i])
    return (sumOr, sumAnd)

groups_data = split_entries_up(data)
puzzle1, puzzle2 = check_everyone(groups_data)
print(puzzle1,puzzle2)