# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), 'day-01-report-repair/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    inputLength = len(data)
    # print(inputLength)

    for i in range(0, inputLength):
        a = int(data[i])

        for j in range(i+1, inputLength):
            b = int(data[j])

            # print(str(a) + " and " + str(b))
            
            if a + b  == 2020:
                return('Sum is: ' + str(a+b) + ". " + str(a) + ", " + str(b) + ' and multiplied together is ' + str(a*b))

print(find_result_part_one())

# =================================================================
# LOGIC - PART TWO
# =================================================================

def find_result_part_two():
    inputLength = len(data)
    # print(inputLength)

    for i in range(0, inputLength):
        a = int(data[i])

        for j in range(i+1, inputLength):
            b = int(data[j])

            for k in range(j+1, inputLength):
                c = int(data[k])

                # print(str(a) + " and " + str(b) + " and " + str(c))
            
                if a + b + c  == 2020:
                    return('Sum is: ' + str(a+b+c) + ". " + str(a) + ", " + str(b) + ", " + str(c) + ' and multiplied together is ' + str(a*b*c))

print(find_result_part_two())