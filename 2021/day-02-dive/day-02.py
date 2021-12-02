# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2021/day-02-dive/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

x = 0
y = 0

for instruction in data:
    direction = instruction.split()[0]
    units = int(instruction.split()[1])
    if direction == 'forward':
        x += units
    elif direction == 'up':
        y -= units
    elif direction == 'down':
        y += units

# print(x * y)

# =================================================================
# LOGIC - PART TWO
# =================================================================

x = 0
y = 0
aim = 0

for instruction in data:
    direction = instruction.split()[0]
    units = int(instruction.split()[1])
    if direction == 'forward':
        x += units
        y += (aim * units)
    elif direction == 'up':
        aim -= units
    elif direction == 'down':
        aim += units

# print(x * y)
