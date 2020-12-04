# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os
import pandas as pd

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), 'day-04-passport-processing/')

with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
# with open(os.path.join(data_location, 'input_ptwo_one.txt'), 'r') as f:
# with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

passportData = []
passport = ""
for line in data:
    if line != "":
        passport += " " + line
    else:    
        passportData.append(passport)
        passport = ""
passportData.append(passport)

# print(passportData)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def find_result_part_one():
    inputLength = len(passportData)
    validCount = 0

    for i in range(0, inputLength):
        passport = passportData[i].split()
        # print(passport)
        passportDict = {}
        for field in passport:
            passportDict[field[0:3]] = field[4:]
        
        numFields = len(passportDict)
        if numFields == 8:
            validCount += 1
        elif numFields == 7 and "cid" not in passportDict:
            validCount += 1
    
    return validCount

# =================================================================
# LOGIC - PART TWO
# =================================================================

def validatePassport(passport):
    byr = passport["byr"]
    iyr = passport["iyr"]
    eyr = passport["eyr"]
    hgt = passport["hgt"]
    hcl = passport["hcl"]
    ecl = passport["ecl"]
    pid = passport["pid"]

    if not (len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002):
        # print(byr)
        return 0
    if not (len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020):
        # print(iyr)
        return 0
    if not (len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030):
        # print(eyr)
        return 0
    if not (hcl[0] == "#" and len(hcl) == 7 and hcl[1:].isalnum()):
        return 0
    if not(ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        # print(ecl)
        return 0
    if not(len(pid) == 9 and pid.isnumeric()):
        # print(pid)
        return 0

    if hgt.find("cm") != -1:
        if not(int(hgt[:hgt.index("cm")]) >= 150 and int(hgt[:hgt.index("cm")]) <= 193):
            # print(hgt + " value: " + hgt[:hgt.index("cm")])
            return 0
    elif hgt.find("in") != -1:
        if not(int(hgt[:hgt.index("in")]) >= 59 and int(hgt[:hgt.index("in")]) <= 76):
            # print(hgt + " value: " + hgt[:hgt.index("in")])
            return 0
    else:
        # print(pid)
        return 0

    return 1

def find_result_part_two():
    inputLength = len(passportData)
    validCount = 0

    for i in range(0, inputLength):
        passport = passportData[i].split()
        # print(passport)
        passportDict = {}
        for field in passport:
            passportDict[field[0:3]] = field[4:]
        
        numFields = len(passportDict)
        if numFields == 8:
            validCount += validatePassport(passportDict)
        elif numFields == 7 and "cid" not in passportDict:
            validCount += validatePassport(passportDict)
    
    return validCount
# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())