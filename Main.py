from CalcUnit import *


def get_expression() -> str:
    string = None
    try:
        string = input("Please enter a mathematic expression:\n")
    except EOFError as eof:
        print("EOF Error")
    return string


def main():
    expression = get_expression()
    calculate_expression(expression)


if __name__ == "__main__":
    main()
