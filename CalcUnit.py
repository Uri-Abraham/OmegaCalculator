from Parser import *


def calculate_expression(exp: str) -> float:
    expression = parse_to_list(exp)
    while len(expression) > 1:
        remove_extra_parentheses(expression)
        next_op_index = find_max_kdimut(expression)
        op_type = op_dict[expression[next_op_index]].get_op_type()
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
    print(expression)


def find_max_kdimut(exp: list) -> int:
    index = -1
    max_kdimut = 0
    parentheses_bonus = 0
    for i in range(len(exp)):
        if exp[i] == '(':
            parentheses_bonus += 10
        elif exp[i] == ')':
            parentheses_bonus -= 10
        elif exp[i] in op_dict:
            if op_dict[exp[i]].get_kdimut() + parentheses_bonus > max_kdimut:
                index = i
                max_kdimut = op_dict[exp[i]].get_kdimut()
            else:
                return index
    return index
