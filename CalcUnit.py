from Parser import *


def calculate_expression(exp : str) -> float:
    l = parse_to_list(exp)
    print(l)