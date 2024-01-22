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
    """
    checks if the string contains illegal symbols, exits if it does
    :param exp: the expression string
    :return: None
    """
    chars_in_expression = set(exp)
    if not chars_in_expression.issubset(acceptable_chars):
        print("It appears the expression contains unknown symbols")
        exit()


def str_to_num(num: str) -> float:
    """
    converts a string to float
    :param num: the number in string type
    :return: the number as a float
    """
    try:
        float(num)
    except (ValueError, TypeError):
        print("Decimal dot at an illegal place")
        exit()
    return float(num)


def parse_to_list(exp: str) -> list:
    """
    gets the mathematical expression as a string and converts it to a list where each element is an operator,
    operand or a parentheses
    :param exp: the mathematical expression as a string
    :return: the mathematical expression in a list format
    """
    try:
        initial_validation(exp)
    except TypeError:
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
    """
    removes redundant parentheses from the list
    :param exp: the mathematical expression as a list
    :return: the mathematical expression as a list
    """
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
    """
    checks for binary minuses that should be unary minuses and replaces them
    :param exp: the mathematical expression as a list
    :return: mathematical expression as a list
    """
    if len(exp) > 1 and exp[0] == '-':
        if isinstance(exp[1], float) or exp[1] == '(' or exp[1] == '-':
            exp[0] = "U-"
    i = 1
    while i < len(exp) - 1:
        if exp[i] == '-':
            if (isinstance(exp[i + 1], float) or exp[i + 1] == '(') and (
                    not isinstance(exp[i - 1], float) and exp[i - 1] != ')'):
                exp[i] = "U-"
                i = 0
            elif exp[i + 1] == "U-" and not isinstance(exp[i - 1], float) and not exp[i - 1] in ")!#":
                exp.pop(i)
                exp.pop(i)
                i = 0
            i += 1
        else:
            i += 1
    for i in range(1, len(exp)):
        if exp[i-1] in op_dict:
            if op_dict[exp[i - 1]].get_op_type() == 3 and exp[i] == "U-":
                exp[i] = "-"
    while exp[0] == "U-" and exp[1] == "U-":
        exp.pop(0)
        exp.pop(0)
    return exp


def check_parentheses_imbalance(exp: list) -> bool:
    """
    checks if there is a legal number a parentheses in the mathematical expression.
    :param exp: the mathematical expression as a list
    :return: true if there's parentheses balance, false otherwise
    """
    opening_p_count = 0
    closing_p_count = 0
    for i in range(len(exp)):
        if exp[i] == '(':
            opening_p_count += 1
        elif exp[i] == ')':
            closing_p_count += 1
    return opening_p_count == closing_p_count
