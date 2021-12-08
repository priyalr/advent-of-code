# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
import math

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2021/day-08-seven-segment-search/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

cleanedData = []
for line in data:
    line = line.split(" | ")
    signals = line[0].split()
    outputs = line[1].split()
    cleanedData.append((signals, outputs))
data = cleanedData

# print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================
def part_one():
    # How many segments are used in each
    digitsDisplay = {0: 6
                    , 1: 2
                    , 2: 5
                    , 3: 5
                    , 4: 4
                    , 5: 5
                    , 6: 6
                    , 7: 3
                    , 8: 7
                    , 9: 6}

    # Counting only digits in the output values 
    # (the part after | on each line)
    outputsCombined = []
    for line in data:
        outputs = line[1]
        for item in outputs:
            outputsCombined.append(item)
    # print(outputsCombined)

    countAppearances = 0
    for item in outputsCombined:
        countSegments = len(set(item))
        if countSegments in (2, 3, 4, 7):
            countAppearances += 1

    return(countAppearances)

# =================================================================
# LOGIC - PART TWO
# =================================================================
def part_two():
    return(None)

# =================================================================
# MAIN
# =================================================================
if __name__ == '__main__':
    print("Part one result is: " , str(part_one()))
    # print("Part two result is: " , str(part_two()))