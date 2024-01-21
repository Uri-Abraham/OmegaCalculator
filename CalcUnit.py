import sys

from Parser import *


def calculate_expression(exp: str) -> float:
    expression = parse_to_list(exp)
    if not check_parentheses_imbalance(expression):
        print("Odd number of parentheses")
        exit()
    if len(expression) == 1:
        try:
            expression = float(expression[0])
            return expression
        except ValueError as e:
            print("it's just a lonely symbol")
            exit()
    expression = remove_extra_parentheses(expression)
    expression = check_unary_minuses(expression)
    while len(expression) > 1:
        next_op_index = find_max_kdimut(expression)
        if next_op_index == -1 and len(expression) > 1:
            print("there appears to be missing operators")
            exit()
        op_type = op_dict[expression[next_op_index]].get_op_type()
        expression = do_next_operation(expression, next_op_index, op_type)
    return expression[0]


def do_next_operation(expression: list, next_op_index: int, op_type: int) -> list:
    if op_type == 1:
        if len(expression) - 1 > next_op_index >= 1:
            expression[next_op_index] = op_dict[expression[next_op_index]].binary_operation(
                expression[next_op_index - 1],
                expression[next_op_index + 1])
            expression.pop(next_op_index - 1)
            expression.pop(next_op_index)
        else:
            print("Illegal operator placement")
            exit()
    elif op_type == 2:
        if len(expression) - 1 > next_op_index:
            if expression[next_op_index] == "~":
                expression = tilda_special_case(expression, next_op_index)
            expression[next_op_index] = op_dict[expression[next_op_index]].unary_operation(
                expression[next_op_index + 1])
            expression.pop(next_op_index + 1)
        else:
            print("Illegal operator placement")
            exit()
    elif op_type == 3:
        if next_op_index >= 1:
            expression[next_op_index] = op_dict[expression[next_op_index]].unary_operation(
                expression[next_op_index - 1])
            expression.pop(next_op_index - 1)
        else:
            print("Illegal operator placement")
            exit()
    expression = remove_extra_parentheses(expression)
    return expression


def find_max_kdimut(exp: list) -> int:
    index = -1
    max_kdimut = 0
    parentheses_bonus = 0
    for i in range(len(exp)):
        if exp[i] == '(':
            parentheses_bonus += 10
        elif exp[i] == ')':
            parentheses_bonus -= 10
        elif exp[i] == float("inf") or exp[i] == float("-inf"):
            print("it appears we've reached to infinity and beyond")
            exit()
        elif exp[i] in op_dict:
            if op_dict[exp[i]].get_kdimut() + parentheses_bonus > max_kdimut:
                index = i
                max_kdimut = op_dict[exp[i]].get_kdimut() + parentheses_bonus
            else:
                return index
    return index


def tilda_special_case(exp: list, tilda_index: int) -> list:
    if exp[tilda_index + 1] == "U-":
        if tilda_index + 2 < len(exp):
            exp[tilda_index + 1] = op_dict["U-"].unary_operation(exp[tilda_index + 2])
            exp.pop(tilda_index + 2)
        else:
            print("Illegal tilda placement")
    return exp
