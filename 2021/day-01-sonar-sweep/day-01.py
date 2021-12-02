# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2021/day-01-sonar-sweep/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

data = list(map(int, data))

# print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

numSweeps = len(data)
numChanges = 0
for i in range(1 ,numSweeps):
    if data[i] > data[i-1] : numChanges += 1

# print(numChanges)

# =================================================================
# LOGIC - PART TWO
# =================================================================

numSweeps = len(data)
numChanges = 0
for i in range(3 ,numSweeps):
    if sum(data[i-2:i+1]) > sum(data[i-3:i]) : numChanges += 1

# print(numChanges)