# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
import copy
from functools import lru_cache

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), 'day-10-adapter-array')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
# with open(os.path.join(data_location, 'input_larger.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

inputLength = len(data)
for i in range(inputLength):
    data[i] = int(data[i])

data = sorted(data)
# print(data)

inputLength = len(data)

data_two = copy.deepcopy(data)
data_two.append(0)
highestAddOn = data_two[inputLength-1] 
data_two.append(highestAddOn+3)
data_two = sorted(data_two)
# print(data_two)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    oneJoltDiffs = 1
    threeJoltDiffs = 1
    i = 0
    while i < inputLength-1:
        currentNum = data[i]
        for j in range(i+1, i+4):
            nextNum = data[j]
            diff = nextNum - currentNum
            # print("Curr: " + str(currentNum) + " Next: " + str(nextNum) + " Diff: " + str(diff))
            if diff <= 3:
                i = j
                if diff == 1:
                    oneJoltDiffs += 1
                elif diff == 3:
                    threeJoltDiffs += 1
                break
    print("One jolt: " + str(oneJoltDiffs) + " Three jolt: " + str(threeJoltDiffs))

    return oneJoltDiffs * threeJoltDiffs
# =================================================================
# LOGIC - PART TWO
# =================================================================
@lru_cache() # called with the same i lots of times, save the recent calls
def find_result_part_two(i):
    currentNum = data_two[i]
    if i == len(data_two) - 1:
        # print("Curr: " + str(currentNum))
        return 1

    tot = 0
    for j in range(i + 1, min(i + 4, len(data_two))):
        nextNum = data_two[j]
        diff = nextNum - currentNum
        if diff <= 3:
            # print("Curr: " + str(currentNum) + " Next: " + str(nextNum) + " Diff: " + str(diff) + " Total: " + str(tot))
            tot += find_result_part_two(j)

    return tot

# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two(0))