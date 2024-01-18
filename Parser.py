from Operators.Operator import *
from Operators.BinaryOperators.Addition import *
from Operators.BinaryOperators.Subtraction import *
from Operators.BinaryOperators.Division import *
from Operators.BinaryOperators.Multiplication import *
from Operators.BinaryOperators.Power import *
from Operators.BinaryOperators.Modulo import *
from Operators.BinaryOperators.Average import *
from Operators.BinaryOperators.Maximum import *
from Operators.BinaryOperators.Minimum import *
from Operators.UnaryOperators.Tilda import *
from Operators.UnaryOperators.Factorial import *

acceptable_chars = set('0123456789. +-*/^@$&%~!#()')

op_dict = {
    "+": Plus(1, 1),
    "-": Sub(1, 1),
    "*": Mul(2, 1),
    "/": Div(2, 1),
    "^": Pow(3, 1),
    "%": Modulo(4, 1),
    "@": Avg(5, 1),
    "$": Max(5, 1),
    "&": Min(5, 1),
    "~": Tilda(6, 2),
    "!": Factorial(6, 3)
}


def initial_validation(exp: str) -> bool:
    chars_in_expression = set(exp)
    if chars_in_expression.issubset(acceptable_chars):
        return True
    else:
        print("It appears the expression contains unknown symbols")
        return False


def str_to_num(num: str) -> float:
    try:
        float(num)
    except Exception as e:
        print("Error!")
        exit()
    return float(num)


def parse_to_list(exp: str) -> list:
    if not initial_validation(exp):
        exit()
    exp = exp.replace(" ", "")
    infix_exp = []
    count = 0
    i = 0
    while i < len(exp):
        if exp[i].isdigit():
            while exp[i].isdigit() or exp[i] == '.':  # (exp[i].isdigit() or exp[i] == '.') and i < len(exp)
                count += 1
                i += 1
                if not i < len(exp):
                    break
            infix_exp.append(str_to_num(exp[i - count: i]))
            count = 0
        elif exp[i] == '.':
            print("decimal dot at an illegal place")
            exit()
        else:
            infix_exp.append(exp[i])
            i += 1
    return infix_exp


def remove_extra_parentheses(exp: list) -> list:
    for i in range(len(exp) - 2):
        if exp[i] == '(' and exp[i+2] == ')':
            exp.pop(i)
            exp.pop(i+1)
    return exp