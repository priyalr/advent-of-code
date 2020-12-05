# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
import pandas as pd

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), 'day-05-binary-boarding/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    maxSeatID = 0
    maxSeat = ""
    for aSeat in data:
        rowInstruction = aSeat[0:7]
        colInstruction = aSeat[-3:]

        lower = 0
        upper = 127
        for letter in rowInstruction:
            if letter == 'F':
                upper = (lower + upper) // 2
                # print(aSeat + " " + letter + " lower, upper: " + str(lower) + " " + str(upper))
            else: 
                lower = ((lower + upper) // 2) + 1
                # print(aSeat + " " + letter + " lower, upper: " + str(lower) + " " + str(upper))
        
        finalRow = min(lower, upper)

        lower = 0
        upper = 7
        for letter in colInstruction:
            if letter == 'L':
                upper = (lower + upper) // 2
                # print(aSeat + " " + letter + " lower, upper: " + str(lower) + " " + str(upper))
            else: 
                lower = ((lower + upper) // 2) + 1
                # print(aSeat + " " + letter + " lower, upper: " + str(lower) + " " + str(upper))
        finalCol = min(lower, upper)
        # # print(str(finalRow) + " " + str(finalCol))

        seatID = (finalRow * 8) + finalCol
        if seatID > maxSeatID:
            maxSeatID = seatID
            maxSeat = aSeat

        # print(str(aSeat) + " " + str(seatID)

    return [maxSeatID, maxSeat]

# =================================================================
# LOGIC - PART TWO
# =================================================================

def getSeatInfo():
    seatData = []
    for aSeat in data:
        rowInstruction = aSeat[0:7]
        colInstruction = aSeat[-3:]

        lower = 0
        upper = 127
        for letter in rowInstruction:
            if letter == 'F':
                upper = (lower + upper) // 2
                # print(aSeat + " " + letter + " lower, upper: " + str(lower) + " " + str(upper))
            else: 
                lower = ((lower + upper) // 2) + 1
                # print(aSeat + " " + letter + " lower, upper: " + str(lower) + " " + str(upper))
        
        finalRow = min(lower, upper)

        lower = 0
        upper = 7
        for letter in colInstruction:
            if letter == 'L':
                upper = (lower + upper) // 2
                # print(aSeat + " " + letter + " lower, upper: " + str(lower) + " " + str(upper))
            else: 
                lower = ((lower + upper) // 2) + 1
                # print(aSeat + " " + letter + " lower, upper: " + str(lower) + " " + str(upper))
        finalCol = min(lower, upper)
        # # print(str(finalRow) + " " + str(finalCol))

        seatData.append([finalRow, finalCol])
        # print(str(aSeat) + " " + str(seatID)

    return seatData

def find_result_part_two():
    seatData = getSeatInfo()

    seat_df = pd.DataFrame(seatData, columns=['row', 'col'])
    seat_df = seat_df.sort_values(by=['row', 'col'])
    seat_df['present'] = 1
    pd.set_option('display.max_rows', seat_df.shape[0]+1)
    seat_df = seat_df.pivot(index='row', columns = 'col', values ='present')
    # print(seat_df)
    seat_df['missing'] = seat_df.isnull().sum(axis=1)
    # print(seat_df)

    return (seat_df.query(' missing == 1' ).head(1).isnull())

# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())