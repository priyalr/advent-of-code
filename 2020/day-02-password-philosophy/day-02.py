# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2020/day-02-password-philosophy/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    validPwdCount = 0

    for line in data:
        minCount = int(line[:line.find("-")])
        maxCount = int(line[line.find("-")+1 : line.find(" ")])
        letter = (line.split()[1])[0]
        pwd = line.split()[2]

        occurences = pwd.count(letter)
        if occurences >= minCount and occurences <= maxCount:
            validPwdCount += 1

    return(validPwdCount)

# =================================================================
# LOGIC - PART TWO
# =================================================================

def find_result_part_two():
    validPwdCount = 0

    for line in data:
        posOne = int(line[:line.find("-")])-1
        posTwo = int(line[line.find("-")+1 : line.find(" ")])-1
        letter = (line.split()[1])[0]
        pwd = line.split()[2]

        posOneCount = 0
        posTwoCount = 0
        if pwd[posOne] == letter:
            posOneCount += 1
        if pwd[posTwo] == letter:
            posTwoCount += 1

        if posOneCount + posTwoCount == 1:
            validPwdCount += 1

    return(validPwdCount)

# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())