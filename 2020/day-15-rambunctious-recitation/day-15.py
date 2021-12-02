# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
from itertools import product

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), 'day-15-rambunctious-recitation/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()
    data = data[0].split(",")

data = [int(number) for number in data]

# print(data)
inputLength = len(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    turnCount = 1
    spokenDict = {}
    previousNum = 0
    while turnCount <= 2020:
        if turnCount <= inputLength:
            spokenNum = data[turnCount-1]
            spokenDict[spokenNum] = [turnCount]
            # print("Starting list, turn:  " + str(turnCount) + ", num = " + str(spokenNum))
            # print(spokenDict)
            previousNum = spokenNum
            turnCount += 1
        else:
            # print(str(previousNum) + " " + str(spokenDict) + " " + str(turnCount))
            if previousNum in spokenDict and len(spokenDict[previousNum]) > 1:
                spokenNum = spokenDict[previousNum][-1] - spokenDict[previousNum][-2]
                # print("Previously spoken, turn: " + str(turnCount) + ", num = " + str(spokenNum))
            else:
                spokenNum = 0
                # print("First time it was spoken, turn: " + str(turnCount) + ", num = " + str(spokenNum))

            if spokenNum in spokenDict:
                spokenDict[spokenNum].append(turnCount)
            else:
                spokenDict[spokenNum] = [turnCount]
            previousNum = spokenNum
            turnCount += 1
        
    return spokenNum

# =================================================================
# LOGIC - PART TWO
# =================================================================

def find_result_part_two():
    turnCount = 1
    spokenDict = {}
    previousNum = 0
    while turnCount <= 30000000:
        if turnCount <= inputLength:
            spokenNum = data[turnCount-1]
            spokenDict[spokenNum] = [turnCount]
            # print("Starting list, turn:  " + str(turnCount) + ", num = " + str(spokenNum))
            # print(spokenDict)
            previousNum = spokenNum
            turnCount += 1
        else:
            # print(str(previousNum) + " " + str(spokenDict) + " " + str(turnCount))
            if previousNum in spokenDict and len(spokenDict[previousNum]) > 1:
                spokenNum = spokenDict[previousNum][-1] - spokenDict[previousNum][-2]
                # print("Previously spoken, turn: " + str(turnCount) + ", num = " + str(spokenNum))
            else:
                spokenNum = 0
                # print("First time it was spoken, turn: " + str(turnCount) + ", num = " + str(spokenNum))

            if spokenNum in spokenDict:
                spokenDict[spokenNum].append(turnCount)
            else:
                spokenDict[spokenNum] = [turnCount]
            previousNum = spokenNum
            turnCount += 1
        
    return spokenNum
    
# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())