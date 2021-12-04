# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2021/day-04-giant-squid/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

numbersCalled = data[0].split(",")
# print(numbersCalled)

boardsLines = data[2:]
boardsLines = [line.split() for line in boardsLines]
boardsLines.append([])

# print(boardsLines)

boardsDict = {}
board = []
i = 0
for line in boardsLines:
    if len(line) == 0:
        boardsDict[i] = board
        board = []
        i += 1
    else:
        board.append(line)

# print(boardsDict)

boardsMarkings = boardsDict.copy()
for i in range(len(boardsMarkings)):
    boardsMarkings[i] = [[False, False, False, False, False] for i in range(5)]

# print(boardsMarkings)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def play_bingo_part_one():
    numBoards = len(boardsDict)

    # Call out a number
    for currentNum in numbersCalled:
        # Mark the number on each board
        for boardNum in boardsDict:
            currentBoard = boardsDict[boardNum]
            for i in range(5):
                for j in range(5):
                    if currentBoard[i][j] == currentNum:
                        boardsMarkings[boardNum][i][j] = True

            # Check if a row or column has been completed
            # Return the last called number
            for i in range(5):
                if boardsMarkings[boardNum][i].count(True) == 5:
                    return(currentNum, boardNum, currentBoard, boardsMarkings[boardNum])
        
            for i in range(5):
                columnTotal = 0
                for j in range(5):
                    if boardsMarkings[boardNum][j][i] == True:
                        columnTotal += 1
                if columnTotal == 5:
                    return(currentNum, boardNum, currentBoard, boardsMarkings[boardNum])


# Add up all uncalled numbers
def add_up_unmarked_numbers(wonBoard, wonBoardsMarkings):
    sum_unmarked = 0
    for i in range(5):
        for j in range(5):
            if wonBoardsMarkings[i][j] == False:
                sum_unmarked += int(wonBoard[i][j])
    return sum_unmarked

# =================================================================
# LOGIC - PART TWO
# =================================================================

def play_bingo_part_two():
    numBoards = len(boardsDict)
    boardsWonCount = 0

    # Call out a number
    for currentNum in numbersCalled:
        # Mark the number on each board
        for boardNum in boardsDict:
            currentBoard = boardsDict[boardNum]
            for i in range(5):
                for j in range(5):
                    if currentBoard[i][j] == currentNum:
                        boardsMarkings[boardNum][i][j] = True

            # Check if a row or column has been completed
            # Return the last called number
            for i in range(5):
                if boardsMarkings[boardNum][i].count(True) == 5:
                    boardsWonCount += 1
                    if boardsWonCount == numBoards:
                        return(currentNum, boardNum, currentBoard, boardsMarkings[boardNum])
                    else:
                        boardsDict[boardNum] = [['', '', '', '', ''] for i in range(5)]
                        boardsMarkings[boardNum] = [[False, False, False, False, False] for i in range(5)]
        
            for i in range(5):
                columnTotal = 0
                for j in range(5):
                    if boardsMarkings[boardNum][j][i] == True:
                        columnTotal += 1
                if columnTotal == 5:
                    boardsWonCount += 1
                    if boardsWonCount == numBoards:
                        return(currentNum, boardNum, currentBoard, boardsMarkings[boardNum])
                    else:
                        boardsDict[boardNum] = [['', '', '', '', ''] for i in range(5)]
                        boardsMarkings[boardNum] = [[False, False, False, False, False] for i in range(5)]

# =================================================================
# PLAY
# =================================================================
if __name__ == '__main__':
    results = play_bingo_part_one()
    sum_unmarked = add_up_unmarked_numbers(results[2], results[3])
    print("Final score is: ", str(sum_unmarked * int(results[0])))
    results = play_bingo_part_two()
    sum_unmarked = add_up_unmarked_numbers(results[2], results[3])
    print("Final score is: ", str(sum_unmarked * int(results[0])))