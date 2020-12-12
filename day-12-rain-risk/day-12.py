# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), 'day-12-rain-risk/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    #              0 ,  1 ,  2 ,  3
    directions = ['N', 'E', 'S', 'W']
    currDirection = 1
    northSouthValue = 0
    eastWestValue = 0

    for instruction in data:
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'F':
            if currDirection == 1: #East
                eastWestValue += value
            elif currDirection == 3: #West
                eastWestValue += -value
            elif currDirection == 0: #North
                northSouthValue += value
            elif currDirection == 2: #south
                northSouthValue += -value
            else:
                print(instruction + " " + str(currDirection))
        elif action == "R":
            nextDirection = 0
            if value == 90:
                nextDirection += 1
            elif value == 180:
                nextDirection += 2
            elif value == 270:
                nextDirection += 3
            elif value == 360:
                nextDirection += 4
            else:
                print(instruction)
            # print(instruction + " " + str(directions[currDirection]) + " " + str((currDirection + nextDirection) % 4 ) + " " + str(directions[(currDirection + nextDirection) % 4 ])) 
            currDirection = (currDirection + nextDirection) % 4 
        elif action == "L":
            nextDirection = 0
            if value == 90:
                nextDirection -= 1
            elif value == 180:
                nextDirection -= 2
            elif value == 270:
                nextDirection -= 3
            elif value == 360:
                nextDirection -= 4
            else:
                print(instruction)   
            # print(instruction + " " + str(directions[currDirection]) + " " + str((currDirection + nextDirection) % 4 ) + " " + str(directions[(currDirection + nextDirection) % 4 ]))   
            currDirection = (currDirection + nextDirection) % 4       
        elif action == "N":
            northSouthValue += value
        elif action == "S":
            northSouthValue += -value
        elif action == "E":
            eastWestValue += value
        elif action == "W":
            eastWestValue += -value
        
        # print(action + " " + str(value) + ", Dir: " + directions[currDirection] + ", East " + str(eastWestValue) + ", North: " + str(northSouthValue))

    return abs(northSouthValue) + abs(eastWestValue)
# =================================================================
# LOGIC - PART TWO
# =================================================================

def find_result_part_two():
    #              0 ,  1 ,  2 ,  3
    directions = ['N', 'E', 'S', 'W']
    currDirection = 1
    northSouthValue = 0
    eastWestValue = 0
    wayPointNorthSouthValue = 1
    wayPointEastWestValue = 10

    for instruction in data:
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'F':
            eastWestValue += (wayPointEastWestValue * value)
            northSouthValue += (wayPointNorthSouthValue * value)

        elif action == "R":
            nextDirection = 0
            if value == 90:
                nextDirection += 1
                wayPointEastWestValue, wayPointNorthSouthValue = wayPointNorthSouthValue, -wayPointEastWestValue
            elif value == 180:
                nextDirection += 2
                wayPointEastWestValue, wayPointNorthSouthValue = -wayPointEastWestValue, -wayPointNorthSouthValue
            elif value == 270:
                nextDirection += 3
                wayPointEastWestValue, wayPointNorthSouthValue = -wayPointNorthSouthValue, wayPointEastWestValue
            elif value == 360:
                nextDirection += 4
            else:
                print(instruction)
            # print(instruction + " " + str(directions[currDirection]) + " " + str((currDirection + nextDirection) % 4 ) + " " + str(directions[(currDirection + nextDirection) % 4 ])) 
            currDirection = (currDirection + nextDirection) % 4 
        elif action == "L":
            nextDirection = 0
            if value == 90:
                nextDirection -= 1
                wayPointEastWestValue, wayPointNorthSouthValue = -wayPointNorthSouthValue, wayPointEastWestValue
            elif value == 180:
                nextDirection -= 2
                wayPointEastWestValue, wayPointNorthSouthValue = -wayPointEastWestValue, -wayPointNorthSouthValue
            elif value == 270:
                nextDirection -= 3
                wayPointEastWestValue, wayPointNorthSouthValue = wayPointNorthSouthValue, -wayPointEastWestValue
            elif value == 360:
                nextDirection -= 4
            else:
                print(instruction)   
            # print(instruction + " " + str(directions[currDirection]) + " " + str((currDirection + nextDirection) % 4 ) + " " + str(directions[(currDirection + nextDirection) % 4 ]))   
            currDirection = (currDirection + nextDirection) % 4       
        elif action == "N":
            wayPointNorthSouthValue += value
        elif action == "S":
            wayPointNorthSouthValue += -value
        elif action == "E":
            wayPointEastWestValue += value
        elif action == "W":
            wayPointEastWestValue += -value
        
        # print("Ship " + action + " " + str(value) + ", Dir: " + directions[currDirection] + ", East " + str(eastWestValue) + ", North: " + str(northSouthValue))
        # print("WP: " + action + " " + str(value) + ", Dir: " + directions[currDirection] + ", East " + str(wayPointEastWestValue) + ", North: " + str(wayPointNorthSouthValue))
        # print("\n")

    return abs(northSouthValue) + abs(eastWestValue)

# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())