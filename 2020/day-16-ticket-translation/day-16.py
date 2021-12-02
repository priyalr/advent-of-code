# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2020/day-16-ticket-translation/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
# with open(os.path.join(data_location, 'input_small_ptwo.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# data = [int(number) for number in data]

rulesDict = {}
tickets = []

# print(data)

for line in data:
    if line == "":
        continue
    elif line[0].isnumeric():
        tickets += [[int(num) for num in line.split(",")]]
    elif line[-1].isnumeric():
        rulesDict[line[0:line.find(":")]] = line[line.find(":")+2:]

# print(rulesDict)
# print(tickets)
inputLength = len(tickets)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    validNums = []
    for oneRule in rulesDict:
        ruleDetails =  rulesDict[oneRule]
        rangeOneLow     = int(ruleDetails[0                                                 :ruleDetails.find("-")                          ])
        rangeOneHigh    = int(ruleDetails[ruleDetails.find("-")+1                           :ruleDetails.find("or")-1                       ])
        rangeTwoLow     = int(ruleDetails[ruleDetails.find("or")+3                          :ruleDetails.find("-", ruleDetails.find("or"))  ])
        rangeTwoHigh    = int(ruleDetails[ruleDetails.find("-", ruleDetails.find("or"))+1   :                                               ])
        rangeNums = list(range(rangeOneLow, rangeOneHigh+1)) + list(range(rangeTwoLow, rangeTwoHigh+1))
        validNums += [num for num in rangeNums]
    validNums = set(validNums)

    ticketScanningErrorRate = 0
    for oneTicket in tickets:
        for value in oneTicket:
            if value in validNums:
                continue
            else:
                ticketScanningErrorRate += value
    return ticketScanningErrorRate

# =================================================================
# LOGIC - PART TWO
# =================================================================

def check_valid_tickets(oneTicket, validRange):
    for value in oneTicket:
        if value in validRange:
            continue
        else:
            return 0
    return 1

def find_result_part_two():
    validNums = []
    validRules = []
    for oneRule in rulesDict:
        ruleDetails =  rulesDict[oneRule]
        rangeOneLow     = int(ruleDetails[0                                                 :ruleDetails.find("-")                          ])
        rangeOneHigh    = int(ruleDetails[ruleDetails.find("-")+1                           :ruleDetails.find("or")-1                       ])
        rangeTwoLow     = int(ruleDetails[ruleDetails.find("or")+3                          :ruleDetails.find("-", ruleDetails.find("or"))  ])
        rangeTwoHigh    = int(ruleDetails[ruleDetails.find("-", ruleDetails.find("or"))+1   :                                               ])
        rangeNums = list(range(rangeOneLow, rangeOneHigh+1)) + list(range(rangeTwoLow, rangeTwoHigh+1))
        validRules.append(rangeNums)
        validNums += [num for num in rangeNums]
    validRange = set(validNums)

    validTickets = []
    for k, oneTicket in enumerate(tickets):
        if check_valid_tickets(oneTicket, validRange) == 1:
            validTickets += [k]

    fieldsPerTicket = []
    numValidTickets = len(validTickets)
    for i in range(numValidTickets):
        oneTicket = tickets[validTickets[i]]
        ticketFields = []
        for value in oneTicket:
            validFields = []
            for k, ruleRange in enumerate(validRules):
                if value in ruleRange:
                    # print(str(value) + " " + str(k) + " " + str(ruleRange))
                    validFields += [k]
            # print("Valid fields: " + str(validFields))
            ticketFields.append(validFields)
        fieldsPerTicket.append(ticketFields)
    # print(fieldsPerTicket)

    numFields = len(fieldsPerTicket[0])
    possibleFields = []
    for i in range(numFields):
        result = set(fieldsPerTicket[0][i])
        for j in range(numValidTickets):
            result.intersection_update(fieldsPerTicket[j][i])
        possibleFields.append(list(result))
    # print(possibleFields)

    positionsDict = {}
    while len(positionsDict) <= 19:
        for k, positions in enumerate(possibleFields):
            try:
                if len(positions) == 1 and positions[0] not in positionsDict:
                    positionsDict[positions[0]] = k
                    possibleFields[k] = positions.remove(positions[0])
                else:
                    for possiblePosition in positions:
                        if possiblePosition in positionsDict:
                            # print(possiblePosition)
                            positions.remove(possiblePosition)
            except TypeError:
                pass
    # print(positionsDict)
    
    runningMultiplied = 1
    for item in positionsDict:
        if item >= 0 and item <= 5:
            runningMultiplied *= tickets[0][positionsDict[item]]

    return runningMultiplied
    
# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())