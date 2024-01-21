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
from Operators.UnaryOperators.Hashtag import *
from Operators.UnaryOperators.Minus import *

acceptable_chars = set('0123456789. +-*/^@$&%~!#()')

op_dict = {
    "+": Plus(1, 1),
    "-": Sub(1, 1),
    "*": Mul(2, 1),
    "/": Div(2, 1),
    "^": Pow(3, 1),
    "U-": Minus(3.5, 2),
    "%": Modulo(4, 1),
    "@": Avg(5, 1),
    "$": Max(5, 1),
    "&": Min(5, 1),
    "~": Tilda(6, 2),
    "#": Hashtag(6, 3),
    "!": Factorial(6, 3)
}


def initial_validation(exp: str) -> None:
    chars_in_expression = set(exp)
    if not chars_in_expression.issubset(acceptable_chars):
        print("It appears the expression contains unknown symbols")
        exit()


def str_to_num(num: str) -> float:
    try:
        float(num)
    except (ValueError, TypeError) as e:
        print("Decimal dot at an illegal place")
        exit()
    return float(num)


def parse_to_list(exp: str) -> list:
    try:
        initial_validation(exp)
    except TypeError as e:
        exit()
    exp = exp.replace(" ", "")
    if len(exp) == 0:
        print("Empty string!")
        exit()
    infix_exp = []
    count = 0
    i = 0
    while i < len(exp):
        if exp[i].isdigit():
            while exp[i].isdigit() or exp[i] == '.':
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
    i = 0
    while i < len(exp) - 2:
        if exp[i] == '(' and exp[i + 2] == ')':
            exp.pop(i)
            exp.pop(i + 1)
            i = 0
        else:
            i += 1
    return exp


def check_unary_minuses(exp: list) -> list:
    if len(exp) > 1 and exp[0] == '-':
        if isinstance(exp[1], float) or exp[1] == '(':
            exp[0] = "U-"
    i = 1
    while i < len(exp) - 1:
        if exp[i] == '-':
            if (isinstance(exp[i + 1], float) or exp[i + 1] == '(') and (
                    not isinstance(exp[i - 1], float) and exp[i - 1] != ')'):
                exp[i] = "U-"
                i = 0
            elif exp[i + 1] == "U-" and not isinstance(exp[i - 1], float):
                exp.pop(i)
                exp.pop(i)
                i = 0
            i += 1
        else:
            i += 1
    return exp


def check_parentheses_imbalance(exp: list) -> bool:
    opening_p_count = 0
    closing_p_count = 0
    for i in range(len(exp)):
        if exp[i] == '(':
            opening_p_count += 1
        elif exp[i] == ')':
            closing_p_count += 1
    return opening_p_count == closing_p_count
