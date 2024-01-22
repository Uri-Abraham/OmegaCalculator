from CalcUnit import *


def get_expression() -> str:
    """
    get expression string from user and checks it from EOF or empty string
    :return: the mathematical expression in string format
    """
    string = None
    try:
        string = input("Please enter a mathematic expression:\n")
    except EOFError as eof:
        raise SystemExit("EOF Error")
    if len(string) == 0:
        raise SystemExit("Empty expression")
    return string


def main():
    """
    gets the expression from user and prints the result
    :return: None
    """
    expression = get_expression()
    print(calculate_expression(expression))


def main_tests(exp: str) -> float:
    """
    same as main but for testing
    :param exp: the mathematical expression in string
    :return: the value of the expression in float type
    """
    try:
        return calculate_expression(exp)
    except EOFError as e:
        print("EOF error!")
        exit()


if __name__ == "__main__":
    main()
