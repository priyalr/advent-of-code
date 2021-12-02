# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
import copy

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), 'day-09-encoding-error/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

inputLength = len(data)
for i in range(inputLength):
    data[i] = int(data[i])

# print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def check_numbers(i, currNumber, preambleLength):
    for j in range(i-preambleLength, i):
        numOne = data[j]
        # print(str(currNumber) + " " + str(numOne))
        for k in range(j+1, i):
            numTwo = data[k]
            if k != j:
                # print(str(currNumber) + " numOne: " + str(numOne) + " numTwo: " + str(numTwo))
                if numOne + numTwo == currNumber:
                    return True
                    # print("Pair found for: " + str(currNumber) + " numOne: " + str(numOne) + " numTwo: " + str(numTwo))
    return False


def find_result_part_one(preambleLength):
    for i in range(preambleLength, inputLength):
        currNumber = data[i]
        if check_numbers(i, currNumber, preambleLength) == False:
            return (currNumber, i)

    return None

# =================================================================
# LOGIC - PART TWO
# =================================================================

def find_result_part_two():
    for i in range(inputLength-1):
        for j in range(i+1, inputLength):
            rangeSum = sum(data[i:j+1])
            if rangeSum == invalidNumber:
                minNum = min(data[i:j+1])
                maxNum = max(data[i:j+1])
                # print("Sum from: " + str(data[i]) + " to " + str(data[j]) + " is " + str(rangeSum))
                # print("Lowest num: " + str(minNum) + " Highest num: " + str(maxNum) + " and sum is: " + str(minNum + maxNum) )
                return minNum + maxNum

    return None

# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    invalidNumber = find_result_part_one(25)[0]
    print(invalidNumber)
    print(find_result_part_two())