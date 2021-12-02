# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
import copy

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), 'day-08-handheld-halting/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
# with open(os.path.join(data_location, 'input_small_ptwo.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)

instructionsList = []
for instruction in data:
    operation = instruction[0:3]
    argument = int(instruction[4:])
    instructionsList.append([operation, argument, 0])

# print(instructionsList)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    pointer = 0
    acc = 0
    while True:
        operation = instructionsList[pointer][0]
        argument = instructionsList[pointer][1]
        instructionsList[pointer][2] += 1

        # print(instructionsList[pointer])

        if instructionsList[pointer][2] == 2:
            return acc

        if operation == "nop":
            pointer += 1
        elif operation == "acc":
            acc += argument
            pointer += 1
        elif operation == "jmp":
            pointer += argument
        else:
            print("Unexpected operation")

    return acc

# =================================================================
# LOGIC - PART TWO
# =================================================================

def check_program(newInstruction):
    pointer = 0
    acc = 0

    inputLength = len(newInstruction)

    while True:
        if pointer >= inputLength:
            return acc
        operation = newInstruction[pointer][0]
        argument = newInstruction[pointer][1]
        newInstruction[pointer][2] += 1

        if newInstruction[pointer][2] > 1:
            return 0

        if operation == "nop":
            pointer += 1
        elif operation == "acc":
            acc += argument
            pointer += 1
        elif operation == "jmp":
            pointer += argument
        else:
            print("Unexpected operation")

    return acc

def find_result_part_two():
    for i, instruction in enumerate(instructionsList):
        operation = instruction[0]
        if operation == "nop" or operation == "jmp":
            newInstructions = copy.deepcopy(instructionsList)
            if operation == "nop":
                newInstructions[i][0] = "jmp"
            else:
                newInstructions[i][0] = "nop"
            acc = check_program(newInstructions)
            if acc != 0:
                return acc
        else:
            continue
    return acc

# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    # print(find_result_part_one())
    print(find_result_part_two())