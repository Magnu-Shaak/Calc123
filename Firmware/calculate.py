import math

def calculator(operator, a, b):
    if operator == "+":
        return (a + b)
    elif operator == "-":
        return (a - b)
    elif operator == "*":
        return (a * b)
    elif operator == "^":
        return (a ** b)
    elif operator == "/":
        return (a / b)
    elif operator == "%":
        return (a % b)
    elif operator == "|":
        return (a // b)
    else:
        return "Error"