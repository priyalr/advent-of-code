# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2020/day-07-handy-haversacks/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)

bagsDict = {}
for line in data:
    currColour = line[:line.find('bags')].strip()
    line = line.replace("bags", "").replace("bag", "")
    otherColours = line[line.find('contain')+7:-1].strip().split(", ")
    # print(str(currColour) + " " + str(otherColours))
    coloursList = []
    for oneColour in otherColours:
        if oneColour.strip() == "no other":
            quantity = 0
            colour = 'no other'
        else:
            quantity = int(oneColour[:oneColour.find(" ")].strip())
            colour = oneColour[oneColour.find(" "):].strip()
        # print(str(quantity) + " " + colour)
        coloursList.append([quantity, colour])
    bagsDict[currColour] = coloursList

# print(bagsDict)

# =================================================================
# LOGIC - PART ONE
# =================================================================

holdingArray = []
def check_bag_one(targetBag):
    parentsList = []
    for item in bagsDict:
        coloursList = bagsDict[item]
        for oneColour in coloursList:
            if oneColour[1] == targetBag:
                # print(item + " " + targetBag)
                holdingArray.append(item)
                parentsList.append(item)
    if len(parentsList) == 0:
        return [targetBag]
    else:
        for item in parentsList:
            check_bag_one(item)

def find_result_part_one():
    check_bag_one('shiny gold')
    return (len(set(holdingArray)))

# =================================================================
# LOGIC - PART TWO
# =================================================================

def check_bag_two(targetBag):
    if targetBag == "no other":
        return(1)
    else:
        return sum([int(k)*check_bag_two(v) for k, v in bagsDict[targetBag]]) + 1

def find_result_part_two():
    return(check_bag_two('shiny gold')-1)

# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    # print(find_result_part_one())
    print(find_result_part_two())