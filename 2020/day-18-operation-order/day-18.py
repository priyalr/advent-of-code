# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import os

# =================================================================
# READ DATA
# =================================================================

data_location = os.path.join(os.path.abspath(""), '2020/day-18-operation-order/')

# with open(os.path.join(data_location, 'input_small.txt'), 'r') as f:
with open(os.path.join(data_location, 'input.txt'), 'r') as f:
    data = f.read().splitlines()

# print(data)
inputLength = len(data)

# =================================================================
# LOGIC - PART ONE
# =================================================================

def calc(operator, result, num):
    if operator == "+":
        return result + num
    elif operator == "-":
        return result - num
    elif operator == "*":
        return result * num
    elif operator == "/":
        return result/num

def evaluate_expression(expression):
    expression = expression.split(" ")
    expressionLen = len(expression)
    result = int(expression[0])
    operator = ""

    for i in range(1, expressionLen):
        item = expression[i]
        if item in ("+", "-", "*", "/"):   
            operator = item
        else:
            result = calc(operator, result, int(item)) 
    # print(str(expression) + " " + str(result))
    return result


def find_result_part_one():
    runningSum = 0
    for i in range(inputLength):
        expression = data[i]
        expression = expression.strip()
        
        # print(expression)
        while "(" in expression:
            last_open = expression.rfind("(")
            next_close = expression.find(")", last_open)
            # print(str(expression) + " | Open: " + str(last_open) + " Close: " + str(next_close))
            expression = expression[:last_open] + str(evaluate_expression(expression[last_open+1:next_close])) + expression[next_close+1:]
        # print(str(evaluate_expression(expression)))
        runningSum += evaluate_expression(expression)
    return runningSum

# =================================================================
# LOGIC - PART TWO
# =================================================================

def calc_two(operator, result, num):
    if operator == "+":
        return result + num
    elif operator == "-":
        return result - num
    elif operator == "*":
        return result * num
    elif operator == "/":
        return result/num

def evaluate_expression_two(expression):
    expression = expression.split(" ")
    # print(expression)

    while "+" in expression:
        i = expression.index("+")
        numToReplace = calc_two("+", int(expression[i-1]), int(expression[i+1]))
        expression = expression[:i-1] + [numToReplace] + expression[i+2:]
        # print(expression)

    expressionLen = len(expression)
    operator = ""
    result = int(expression[0])
    for i in range(1, expressionLen):
        item = expression[i]
        if item in ("+", "-", "*", "/"):   
            operator = item
        else:
            result = calc_two(operator, result, int(item)) 
    # print(str(expression) + " " + str(result))
    return result


def find_result_part_two():
    runningSum = 0
    for i in range(inputLength):
        expression = data[i]
        expression = expression.strip()
        
        # print(expression)
        while "(" in expression:
            last_open = expression.rfind("(")
            next_close = expression.find(")", last_open)
            # print(str(expression) + " | Open: " + str(last_open) + " Close: " + str(next_close))
            expression = expression[:last_open] + str(evaluate_expression_two(expression[last_open+1:next_close])) + expression[next_close+1:]
        # print(str(evaluate_expression_two(expression)))
        runningSum += evaluate_expression_two(expression)
    return runningSum
    
# =================================================================
# RUN
# =================================================================
if __name__ == "__main__":
    print(find_result_part_one())
    print(find_result_part_two())