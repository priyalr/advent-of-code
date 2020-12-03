# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), 'day-03-toboggan-trajectory/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

mapPattern = []

for line in data:
    lineList = [c for c in line]
    mapPattern.append(lineList)

# print(mapPattern)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    inputLength = len(mapPattern)
    # print(inputLength)
    inputWidth = len(mapPattern[0])
    # print(inputWidth)

    iCurrentPoint = 0
    jCurrentPoint = 0
    currentObject = ""
    treeCount = 0

    while iCurrentPoint < inputLength:
        if jCurrentPoint >= inputWidth:
            for line in mapPattern:
                line.extend(line[0:inputWidth])
        currentObject =  mapPattern[iCurrentPoint][jCurrentPoint]
        # print("At " + str(iCurrentPoint) + ", " + str(jCurrentPoint) + " is: " + currentObject)
        if currentObject == "#":
            treeCount += 1

        iCurrentPoint += 1
        jCurrentPoint += 3

    return(treeCount)

# =================================================================
# LOGIC - PART TWO
# =================================================================

def count_trees(aSlope):
    inputLength = len(mapPattern)
    # print(inputLength)
    inputWidth = len(mapPattern[0])
    # print(inputWidth)

    iCurrentPoint = 0
    jCurrentPoint = 0
    currentObject = ""
    treeCount = 0

    while iCurrentPoint < inputLength:
        # print(str(iCurrentPoint) + " " + str(jCurrentPoint))
        if jCurrentPoint >= inputWidth:
            for line in mapPattern:
                line.extend(line[0:inputWidth])
        currentObject =  mapPattern[iCurrentPoint][jCurrentPoint]
        # print("At " + str(iCurrentPoint) + ", " + str(jCurrentPoint) + " is: " + currentObject)
        if currentObject == "#":
            treeCount += 1

        iCurrentPoint += aSlope[1] # how many steps right
        jCurrentPoint += aSlope[0] # how many steps down

    return(treeCount)

def find_result_part_two():
    multiplied = 1
    
    slopesToCheck = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    for aSlope in slopesToCheck:
        multiplied = multiplied * count_trees(aSlope)

    return(multiplied)

# =================================================================
# LOGIC - BETTER
# =================================================================

def count_trees_better(aSlope):
    inputLength = len(mapPattern)
    # print(inputLength)
    inputWidth = len(mapPattern[0])
    # print(inputWidth)

    iCurrentPoint = 0
    jCurrentPoint = 0
    currentObject = ""
    treeCount = 0

    while iCurrentPoint < inputLength:
        currentObject =  mapPattern[iCurrentPoint % inputWidth][jCurrentPoint]
        if currentObject == "#":
            treeCount += 1

        iCurrentPoint += aSlope[1] # how many steps right
        jCurrentPoint += aSlope[0] # how many steps down

    return(treeCount)

def find_result_better():
    multiplied = 1
    
    slopesToCheck = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    for aSlope in slopesToCheck:
        multiplied = multiplied * count_trees_better(aSlope)

    return(multiplied)

# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())
    print(find_result_better())