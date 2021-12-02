# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
from itertools import product

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2020/day-17-conway-cubes/')

with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
# with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)
inputLength = len(data)

emptyList = ['.'*inputLength for i in range(inputLength)]
data = [emptyList] + [data] + [emptyList]

print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def check_neighbour_cubes(i, j, k, neighbourPositions):
    neighbourCubes = []
    try:
        for onePosition in neighbourPositions:
            neighbourCubes+= data[i+onePosition[0]][j+onePosition[1]][k+onePosition[2]]
    except IndexError:
        pass
    # print(neighbourCubes)
    return neighbourCubes.count("#")

def find_result_part_one():
    neighbourPositions = list(product(range(-1, 2), repeat=3))[1:]

    cycleNum = 1
    
    while cycleNum <= 1:
        newArrangement = []
        for i in range(1, 2):
            newLine = []
            for j in range(inputLength):
                newString = ""
                for k in range(inputLength):    
                    currentcube = data[i][j][k]
                    activeNeighbours = check_neighbour_cubes(i, j, k, neighbourPositions)
                    if currentcube == "#":
                        if activeNeighbours >= 2 and activeNeighbours <= 3:
                            newString += "#"
                        else:
                            newString += "."
                    else:
                        if activeNeighbours == 3:
                            newString += "#"
                        else:
                            newString += "."
                newLine.append(newString)
            newArrangement.append(newLine)
        cycleNum += 1
        print(newArrangement)

    return None

# =================================================================
# LOGIC - PART TWO
# =================================================================

def find_result_part_two():
    return None
    
# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    # print(find_result_part_two())