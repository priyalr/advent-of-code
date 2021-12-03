# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2021/day-03-binary-diagnostic/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

numbersDiagnosticReport = len(data)
numCharacters = len(data[0])
gammaRate = ''
epsilonRate = ''

for i in range(numCharacters):
    zeroCount = 0
    oneCount = 0
    for j in range(numbersDiagnosticReport):
        if data[j][i] == '0': 
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount > oneCount:
        gammaRate += '0'
        epsilonRate += '1'
    else:
        gammaRate += '1'
        epsilonRate += '0'

# print(int(gammaRate, 2) * int(epsilonRate, 2))

# =================================================================
# LOGIC - PART TWO
# =================================================================

numbersDiagnosticReport = len(data)
numCharacters = len(data[0])

oxygenGeneratorNumbers = data.copy()
coTwoScrubberNumbers = data.copy()

i = 0
while len(oxygenGeneratorNumbers) != 1:
    for i in range(numCharacters):
        zeroCount = 0
        oneCount = 0
        mostCommon = ''

        # count occurence of each
        for j in range(numbersDiagnosticReport):
            if oxygenGeneratorNumbers[j][i] == '0': 
                zeroCount += 1
            else:
                oneCount += 1

        # most common character
        if zeroCount > oneCount:
            mostCommon = '0'
        elif oneCount >= zeroCount:
            mostCommon = '1'

        newOxygenGenerator = []
        # go through numbers and remove
        for aNumber in oxygenGeneratorNumbers:
            if aNumber[i] == mostCommon:
                newOxygenGenerator.append(aNumber)

        oxygenGeneratorNumbers = newOxygenGenerator.copy()
        numbersDiagnosticReport = len(oxygenGeneratorNumbers)
        if numbersDiagnosticReport == 1:
            break

numbersDiagnosticReport = len(data)
i = 0
while len(coTwoScrubberNumbers) != 1:
    for i in range(numCharacters):
        zeroCount = 0
        oneCount = 0
        leastCommon = ''

        for j in range(numbersDiagnosticReport):
            if coTwoScrubberNumbers[j][i] == '0': 
                zeroCount += 1
            else:
                oneCount += 1

        if zeroCount <= oneCount:
            leastCommon = '0'
        elif oneCount < zeroCount:
            leastCommon = '1'

        newCoTwoScrubber = []
        for aNumber in coTwoScrubberNumbers:
            if aNumber[i] == leastCommon:
                newCoTwoScrubber.append(aNumber)
        
        coTwoScrubberNumbers = newCoTwoScrubber.copy()
        numbersDiagnosticReport = len(coTwoScrubberNumbers)
        if numbersDiagnosticReport == 1:
            break

# print(int(oxygenGeneratorNumbers[0], 2) * int(coTwoScrubberNumbers[0], 2))

