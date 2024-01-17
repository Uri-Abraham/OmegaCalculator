acceptable_chars = set('0123456789. +-*/^@$&%~!#()')


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
        else:
            infix_exp.append(exp[i])
            i += 1
    return infix_exp
