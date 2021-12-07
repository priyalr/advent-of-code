# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
import math

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2021/day-07-the-treachery-of-whales/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().split(",")

data = [int(fish) for fish in data] 

# print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================
def part_one():
    lowestPosition = min(data)
    highestPosition = max(data)
    print("Lowest is ", str(lowestPosition), ' and highest is ', str(highestPosition))

    result = [0, math.inf]

    for i in range(lowestPosition, highestPosition+1):
        fuel = 0
        for position in data:
            fuel += abs(i-position)
        if fuel < result[1]:
            result[0] = i # align to this position
            result[1] = fuel # this is how much fuel will be required

    return(result)

# =================================================================
# LOGIC - PART TWO
# =================================================================
def part_two():
    lowestPosition = min(data)
    highestPosition = max(data)
    crabCounts = {}
    data.sort()

    result = [0, math.inf]

    for crab in data:
        crabCounts[crab] = data.count(crab)
    # print(crabCounts)

    steps = [0]
    for k in range(0,highestPosition):
        steps.append(k+1)

    orderedCrabs = list(set(data))

    for i in range(lowestPosition, highestPosition+1):
        fuel = 0
        for position in orderedCrabs:
            difference = abs(i-position)
            moves = sum(steps[0:(difference+1)])
            # print("For i = ", str(i), " for crabs at position ", str(position), "they have to move by ", str(difference), " and the fuel used per crab will be ", str(moves))
            fuel += (moves * crabCounts[position])
        if fuel < result[1]:
            result[0] = i # align to this position
            result[1] = fuel # this is how much fuel will be required

    return(result)

# =================================================================
# MAIN
# =================================================================
if __name__ == '__main__':
    # print("Part one result is: " , str(part_one()))
    print("Part two result is: " , str(part_two()))