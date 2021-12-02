# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
import copy
from functools import lru_cache

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2020/day-11-seating-system/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)

inputLength = len(data)
inputWidth = len(data[0])

data_two = copy.deepcopy(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def check_adjacent_seats(i, j, data):
    adjacentSeats = []
    if i-1 >= 0:
        try: adjacentSeats += data[i-1][j]
        except: pass
    if i+1 >= 0:
        try: adjacentSeats += data[i+1][j]
        except: pass
    if j-1 >= 0:
        try: adjacentSeats += data[i][j-1]
        except: pass
    if j+1 >= 0:
        try: adjacentSeats += data[i][j+1]
        except: pass
    if i+1 >= 0 and j+1 >= 0:
        try: adjacentSeats += data[i+1][j+1]
        except: pass
    if i-1 >= 0 and j-1 >= 0:
        try: adjacentSeats += data[i-1][j-1]
        except: pass
    if i+1 >= 0 and j-1 >= 0:
        try: adjacentSeats += data[i+1][j-1]
        except: pass
    if i-1 >= 0 and j+1 >= 0:
        try: adjacentSeats += data[i-1][j+1]
        except: pass
    # print("Curr seat at: " + str(i) + ", " + str(j) + " "  + str(data[i][j] + " " + str(adjacentSeats)))
    return int(adjacentSeats.count("#"))

def find_result_part_one(data):
    round = 0
    # occupiedSeats = 0
    occupiedSeats = []

    while True:
        if round == 0:
            occupiedSeatCount = 0
            for i in range(inputLength):
                row = data[i]
                data[i] = row.replace("L", "#")
                occupiedSeatCount+= data[i].count("#")
            occupiedSeats.append(occupiedSeatCount)
            # print("After round 0, occupied seats = " + str(occupiedSeats[round]) + " "  + str(data) )
            round += 1
        else:
            newSeating = []
            occupiedSeatCount = 0
            for i in range(inputLength):
                updatedRow = ""
                for j in range(inputWidth):
                    currSeat = data[i][j]
                    if currSeat == ".":
                        updatedRow += "."
                    elif currSeat == "L":
                        # print("Curr seat: " + currSeat + " adjacent occupied seats: " + str(check_adjacent_seats(i, j, data)))
                        if check_adjacent_seats(i, j, data) == 0:
                            updatedRow += "#"
                        else:
                            updatedRow += "L"
                    elif currSeat == "#":
                        # print("Curr seat: " + currSeat + " adjacent occupied seats: " + str(check_adjacent_seats(i, j, data)))
                        if check_adjacent_seats(i, j, data) >= 4:
                            updatedRow += "L"
                        else:
                            updatedRow += "#"
                newSeating.append(updatedRow)
                occupiedSeatCount += updatedRow.count("#")
            data = copy.deepcopy(newSeating)
            occupiedSeats.append(occupiedSeatCount)
            # print("After round " + str(round) + " updated seating = " + str(data) + " and occupied seats = " + str(occupiedSeats[round]) )
            if occupiedSeats[round] == occupiedSeats[round-1]:
                return occupiedSeatCount
            round += 1

    return 0
# =================================================================
# LOGIC - PART TWO
# =================================================================
def check_adjacent_seats_two(currI, currJ, data):
    adjacentSeats = []
    for i in range(currI-1, -1, -1): #Up 
        if i >= 0:
            try:
                if data[i][currJ] != ".":
                    # print(1)
                    adjacentSeats += data[i][currJ]
                    break
            except: pass
    for i in range(currI+1, inputLength, 1): #Down 
        if i >= 0:
            try:
                if data[i][currJ] != ".":
                    # print(2)
                    adjacentSeats += data[i][currJ]
                    break
            except: pass
    for j in range(currJ-1, -1, -1): #Left 
        if j >= 0:
            try:
                if data[currI][j] != ".":
                    # print(3)
                    adjacentSeats += data[currI][j]
                    break
            except: pass
    for j in range(currJ+1, inputWidth, 1): #Right 
        if j >= 0:
            try:
                if data[currI][j] != ".":
                    # print(4)
                    adjacentSeats += data[currI][j]
                    break
            except: pass
    for k in range(1, inputLength, 1): #Top left diagonal
        if currI - k >= 0 and currJ - k >= 0:
            try:
                if data[currI - k][currJ - k] != ".":
                    # print(5)
                    adjacentSeats += data[currI - k][currJ - k]
                    break
            except: pass
    for k in range(1, inputLength, 1): #Bottom right diagonal
        if currI + k >= 0 and currJ + k >= 0:
            try:
                if data[currI + k][currJ + k] != ".":
                    # print(6)
                    adjacentSeats += data[currI + k][currJ + k]
                    break
            except: pass
    for k in range(1, inputLength, 1): #Top right
        if currI - k >= 0 and currJ + k >= 0:
            try:
                if data[currI - k][currJ + k] != ".":
                    # print(7)
                    adjacentSeats += data[currI - k][currJ + k]
                    break
            except: pass                                 
    for k in range(1, inputLength, 1): #Bottom left diagonal
        if currI + k >= 0 and currJ - k >= 0:
            try:
                if data[currI + k][currJ - k] != ".":
                    # print(8)
                    adjacentSeats += data[currI + k][currJ - k]
                    break
            except: pass

    # print("Curr seat at: " + str(currI) + ", " + str(currJ) + " "  + str(data[currI][currJ] + " " + str(adjacentSeats)))
    return int(adjacentSeats.count("#"))

def find_result_part_two(data):
    round = 0
    # occupiedSeats = 0
    occupiedSeats = []

    while True:
        if round == 0:
            occupiedSeatCount = 0
            for i in range(inputLength):
                row = data[i]
                data[i] = row.replace("L", "#")
                occupiedSeatCount+= data[i].count("#")
            occupiedSeats.append(occupiedSeatCount)
            # print("After round 0, occupied seats = " + str(occupiedSeats[round]) + " "  + str(data) )
            round += 1
        else:
            newSeating = []
            occupiedSeatCount = 0
            for i in range(inputLength):
                updatedRow = ""
                for j in range(inputWidth):
                    currSeat = data[i][j]
                    if currSeat == ".":
                        updatedRow += "."
                    elif currSeat == "L":
                        # print("Curr seat: " + currSeat + " adjacent occupied seats: " + str(check_adjacent_seats_two(i, j, data)))
                        if check_adjacent_seats_two(i, j, data) == 0:
                            updatedRow += "#"
                        else:
                            updatedRow += "L"
                    elif currSeat == "#":
                        # print("Curr seat: " + currSeat + " adjacent occupied seats: " + str(check_adjacent_seats_two(i, j, data)))
                        if check_adjacent_seats_two(i, j, data) >= 5:
                            updatedRow += "L"
                        else:
                            updatedRow += "#"
                newSeating.append(updatedRow)
                occupiedSeatCount += updatedRow.count("#")
            data = copy.deepcopy(newSeating)
            occupiedSeats.append(occupiedSeatCount)
            # print("After round " + str(round) + " updated seating = " + str(data) + " and occupied seats = " + str(occupiedSeats[round]) )
            if occupiedSeats[round] == occupiedSeats[round-1]:
                return occupiedSeatCount
            round += 1

    return 0
# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one(data))
    print(find_result_part_two(data_two))