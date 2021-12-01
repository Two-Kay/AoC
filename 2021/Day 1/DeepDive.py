data = open("input", "r+")
data = data.read()
data = data.split("\n")

def deep_counting(data=None):
    count = 0
    prev = None
    it = 0
    for entry in data:
        if (prev == None):
            prev = (int)(entry)
        else:
            it += 1
            if((int)(prev) < (int)(entry)):
                count += 1
            prev = entry
    return(count)
    
def slidy_counting(data=None):
    sliding = []
    for i in range(len(data)):
        if((len(data) - i) > 2):
            sliding.append(int(data[i])+int(data[i+1])+int(data[i+2]))
    return(deep_counting(data=sliding))

print(deep_counting(data))
print(slidy_counting(data))