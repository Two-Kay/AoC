file = "2023/Day15/input"


def hash(file):
    output = 0
    sequences = []
    with open(file, "r+") as f:
        for line in f:
            sequences.extend(line.split(","))
    for sequence in sequences:
        val = 0
        for character in sequence:
            val += ord(character)
            val *= 17
            val %= 256
        output += val
    return output


def focal_power(file):
    output = 0
    sequences = []
    boxes = {}
    with open(file, "r+") as f:
        for line in f:
            sequences.extend(line.split(","))
    for sequence in sequences:
        val = 0
        if "=" in sequence:
            sequence_val = sequence.split("=")
            for char in sequence_val[0]:
                val += ord(char)
                val *= 17
                val %= 256
            if val in boxes:
                boxes[val][sequence_val[0]] = int(sequence_val[1])
            else:
                boxes[val] = {}
                boxes[val][sequence_val[0]] = int(sequence_val[1])
        else:
            sequence_val = sequence.strip("-")
            for char in sequence_val:
                val += ord(char)
                val *= 17
                val %= 256
            if val in boxes:
                if sequence_val in boxes[val]:
                    boxes[val].pop(sequence_val)
    for box in boxes:
        i = 1
        for lense in boxes[box]:
            val = box + 1
            val *= i
            i += 1
            val *= boxes[box][lense]
            output += val
    return output


print(focal_power(file))
