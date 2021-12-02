# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2020/day-06-custom-customs')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)

answersData = []
answers = ""
for line in data:
    if line != "":
        answers += " " + line
    else:    
        answersData.append(answers)
        answers = ""
answersData.append(answers)

# print(answersData)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    inputLength = len(answersData)
    answerCount = 0

    for i in range(0, inputLength):
        # Each group
        answers = answersData[i].split()
        # print(answers)
        answersDict = {}
        # numPeople = len(answers)
        for person in answers:
            person = "".join(set(person)) 
            # print(person) 
            for eachAnswer in person:
                if eachAnswer in answersDict:
                    answersDict[eachAnswer] += 1
                else:
                    answersDict[eachAnswer] = 1
        answerCount += len(answersDict)
        # print("Num of people: " + str(numPeople) + " " + str(answersDict))

    return answerCount

# =================================================================
# LOGIC - PART TWO
# =================================================================

def find_result_part_two():
    inputLength = len(answersData)
    answerCount = 0

    for i in range(0, inputLength):
        # Each group
        answers = answersData[i].split()
        # print(answers)
        answersDict = {}
        numPeople = len(answers)
        for person in answers:
            person = "".join(set(person)) 
            # print(person) 
            for eachAnswer in person:
                if eachAnswer in answersDict:
                    answersDict[eachAnswer] += 1
                else:
                    answersDict[eachAnswer] = 1
        # print("Num of people: " + str(numPeople) + " " + str(answersDict))

        for item in answersDict:
            if answersDict[item] == numPeople:
                answerCount += 1
      
    return answerCount


# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())