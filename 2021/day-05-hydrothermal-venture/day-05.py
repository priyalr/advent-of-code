# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2021/day-05-hydrothermal-venture/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# Get points in each line
numLines = len(data)
cleanedData = []
highestNum = 0
for i in range(numLines):
    linePoints = []
    oneLine = data[i].split(" -> ")
    for onePoint in oneLine:
        linePoints.append(int(onePoint.split(",")[0]))
        linePoints.append(int(onePoint.split(",")[1]))
        if int(onePoint.split(",")[0]) > highestNum:
            highestNum = int(onePoint.split(",")[0])
        if int(onePoint.split(",")[1]) > highestNum:
            highestNum = int(onePoint.split(",")[1])
    cleanedData.append(linePoints)
data = cleanedData
# print(data)
# print(highestNum)

overlapGrid = []
for i in range(highestNum+1):
    overlapGrid.append((highestNum+1) * [0])

# print(overlapGrid)

# =================================================================
# LOGIC - PART ONE
# =================================================================
def part_one():
    for oneLine in data:
        x_one = oneLine[0]
        x_two = oneLine[2]
        y_one = oneLine[1]
        y_two = oneLine[3]

        # Check the type of line
        lineType = ''
        if y_one == y_two:
            lineType = 'horizontal'
            x_one = min(oneLine[0], oneLine[2])
            x_two = max(oneLine[0], oneLine[2])
        elif x_one == x_two:
            lineType = 'vertical'
            y_one = min(oneLine[1], oneLine[3])
            y_two = max(oneLine[1], oneLine[3])
        else:
            lineType = 'diagonal'
        # print(oneLine, " is ", lineType)

        # Mark overlap points
        if lineType == 'horizontal':
            for i in range(x_one, x_two+1):
                overlapGrid[y_one][i] += 1
        elif lineType == 'vertical':
            for i in range(y_one, y_two+1):
                overlapGrid[i][x_one] += 1

        # for line in overlapGrid:
        #     print(line)

    dangerousCount = 0
    for oneLine in overlapGrid:
        for onePoint in oneLine:
            if onePoint >= 2:
                dangerousCount += 1
    return(dangerousCount)

# =================================================================
# LOGIC - PART TWO
# =================================================================
def part_two():
    for oneLine in data:
        x_one = oneLine[0]
        x_two = oneLine[2]
        y_one = oneLine[1]
        y_two = oneLine[3]

        xDir = 1
        yDir = 1

        # Check the type of line
        lineType = ''
        if y_one == y_two:
            lineType = 'horizontal'
            x_one = min(oneLine[0], oneLine[2])
            x_two = max(oneLine[0], oneLine[2])
        elif x_one == x_two:
            lineType = 'vertical'
            y_one = min(oneLine[1], oneLine[3])
            y_two = max(oneLine[1], oneLine[3])
        else:
            lineType = 'diagonal'
            if x_two < x_one:
                xDir = -1
            if y_two < y_one:
                yDir = -1

        # Mark overlap points
        if lineType == 'horizontal':
            for i in range(x_one, x_two+1):
                overlapGrid[y_one][i] += 1
        elif lineType == 'vertical':
            for i in range(y_one, y_two+1):
                overlapGrid[i][x_one] += 1
        else:
            numUpdates = max(y_one, y_two) - min(y_one, y_two) + 1
            for i in range(numUpdates):
                overlapGrid[y_one+(i*yDir)][x_one+(i*xDir)] += 1


    dangerousCount = 0
    for oneLine in overlapGrid:
        for onePoint in oneLine:
            if onePoint >= 2:
                dangerousCount += 1
    return(dangerousCount)

# =================================================================
# MAIN
# =================================================================
if __name__ == '__main__':
    # print("Part one dangerous count is: " , str(part_one()))
    print("Part two dangerous count is: " , str(part_two()))