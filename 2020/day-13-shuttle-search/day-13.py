# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
import copy
import math
import numpy as np

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2020/day-13-shuttle-search/')

with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
# with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()
    earliestBus = int(data[0])
    data = data[1].split(",")

data_two = copy.deepcopy(data)
data = list(filter(lambda a: a != 'x', data))
# print(earliestBus)
# print(data)
print(data_two)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    earliestBusTime = 99999999999
    earliestBusID = 0
    for item in data:
        busID = int(item)
        closestBus = 0
        
        if earliestBus % busID == 0:
            closestBus = 0
        else:
            closestBus = busID *  ((earliestBus // busID) + 1)
        
        if closestBus < earliestBusTime:
            earliestBusTime = closestBus
            earliestBusID = busID

    return ((earliestBusTime - earliestBus) * earliestBusID)

# =================================================================
# LOGIC - PART TWO
# =================================================================

def find_result_part_two():
    earliestTime = 0 
    runningProduct = 1
    for (index, busID) in enumerate(data_two):
        if busID == 'x':
            continue
        else:
            busID = int(busID)
            while((earliestTime + index) % busID != 0):
                earliestTime += runningProduct
            runningProduct *= busID
            print("Bus " + str(index) + " ID: " + str(busID) + " Earliest time: " + str(earliestTime) + ", Running product: " + str(runningProduct))
    return earliestTime


# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    # print(find_result_part_one())
    print(find_result_part_two())