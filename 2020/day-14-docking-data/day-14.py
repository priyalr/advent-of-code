# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
from itertools import product

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2020/day-14-docking-data/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
# with open(os.path.join(data_location, 'input_small_ptwo.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)
inputLength = len(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    mask = data[0][7:]
    memoryDict = {}
    # print(mask)
    for i in range(1, inputLength):
        instruction = data[i]
        if instruction[0:4] == "mask":
            mask = instruction[7:] # Update mask
        else:
            memAddress  = int(instruction[instruction.find("[")+1:instruction.find("]")])   # E.g. in mem[8] = 11 -> 8
            memValue    = int(instruction[instruction.find("=")+2:])                        # E.g. in mem[8] = 11 -> 11
            memoryDict[memAddress] = memValue
            binaryMemValue = str(bin(memValue))[str(bin(memValue)).find("b")+1:].zfill(36)  # Create a string of 36 bits

            result = ""
            for i in range(36):
                if mask[i] == "X":                                                          # If it is X, update with the new value
                    # print(binaryMemValue[i])
                    result += binaryMemValue[i]
                else:
                    # print(binaryMemValue[i])
                    result += mask[i]                                                       # Otherwise overwrite with the value in the mask
            resultValue = int(result, 2)                                                    # Convert from 36-bit result binary to int
            memoryDict[memAddress] = resultValue                                            # Add value to the specified memory address
            # print(str(memAddress) + " " + str(memValue) + " " + binaryMemValue + " " + result + " " + str(resultValue))
    
    memorySum = 0 
    for item in memoryDict:
        memorySum += memoryDict[item]                                                       # Sum all values left in memory after it completes
    return memorySum

# =================================================================
# LOGIC - PART TWO
# =================================================================

def generate_possible_values(rVal, repeatVal):
    # Based on how to generate combinations: https://stackoverflow.com/questions/25991292/python-all-possible-combinations-of-0-1-of-length-k
    return list(product(range(rVal), repeat=repeatVal))

def find_result_part_two():
    mask = data[0][7:]
    memoryDict = {}
    # print(mask)
    for i in range(1, inputLength):
        instruction = data[i]
        if instruction[0:4] == "mask":
            mask = instruction[7:]                                                              # Update mask
        else:
            memAddress = int(instruction[instruction.find("[")+1:instruction.find("]")])        # E.g. in mem[8] = 11 -> 8
            memValue = int(instruction[instruction.find("=")+2:])                                  # E.g. in mem[8] = 11 -> 11
            binaryMemValue = str(bin(memAddress))[str(bin(memAddress)).find("b")+1:].zfill(36)  # Create a string of 36 bits

            floatingCount = 0                                                                   # Count how many floating places there are so we can generate combinations later on
            result = ""                                                                         # Result string based on result
            floatingPlaces = []                                                                 # Indexes of the places where there is a floating character
            for i in range(36):                                                                 # Compare to mask and update based on rules
                if mask[i] == "X":
                    result += "X"
                    floatingCount += 1
                    floatingPlaces += [i]
                elif mask[i] == "1":
                    result += "1"
                else:
                    result += binaryMemValue[i]
            # print(str(memAddress) + " " + str(memValue) + " " + binaryMemValue + " " + result + " floating: " + str(floatingCount) + " " + str(floatingPlaces))

            possibleValues = generate_possible_values(2, floatingCount)                         # Possible combinations, e.g. 00, 01, 10, 11
            for item in possibleValues:
                newValue = list(result)                                                         # Make a list from the string so we can replace with the combinations
                for k, v in enumerate(floatingPlaces):
                    newValue[v] = str(item[k])                          
                newValue = int(''.join(newValue), 2)                                            # Convert back from binary to int
                memoryDict[newValue] = memValue                                                 # Update the value at the address (based on newValue)
    
    memorySum = 0                                                                               # Sum all values left in memory after it completes
    for item in memoryDict:
        memorySum += memoryDict[item]
    return memorySum
    

# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())