from Parser import *


def calculate_expression(exp: str) -> float:
    expression = parse_to_list(exp)
    while len(expression) > 1:
        next_op_index = find_max_kdimut(expression)
        op_type = expression[next_op_index].get_op_type()
        if op_type == 1:
            if len(expression)-1 > next_op_index >= 1:
                expression[next_op_index] = expression[next_op_index].binary_operation(expression[next_op_index - 1], expression[next_op_index + 1])
                expression.pop(next_op_index - 1)
                expression.pop(next_op_index)
            else:
                print("Illegal operator placement")
        elif op_type == 2:
            if len(expression)-1 > next_op_index:
                expression[next_op_index] = expression[next_op_index].unary_operation(expression[next_op_index + 1])
                expression.pop(next_op_index+1)
            else:
                print("Illegal operator placement")
        elif op_type == 3:
            if next_op_index >= 1:
                expression[next_op_index] = expression[next_op_index].unary_operation(expression[next_op_index - 1])
                expression.pop(next_op_index-1)
            else:
                print("Illegal operator placement")
    print(expression)


def find_max_kdimut(exp: list) -> int:
    index = -1
    max_kdimut = 0
    for i in range(len(exp)):
        if isinstance(exp[i], Operator):
            if exp[i].get_kdimut() > max_kdimut:
                index = i
                max_kdimut = exp[i].get_kdimut()
    return index
