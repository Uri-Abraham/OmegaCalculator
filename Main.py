from CalcUnit import *


def get_expression() -> str:
    string = None
    try:
        string = input("Please enter a mathematic expression:\n")
    except EOFError as eof:
        raise SystemExit("EOF Error")
    if len(string) == 0:
        raise SystemExit("Empty expression")
    return string


def main():
    expression = get_expression()
    print(calculate_expression(expression))


def main_tests(exp: str) -> float:
    try:
        return calculate_expression(exp)
    except EOFError as e:
        print("EOF error!")
        exit()


if __name__ == "__main__":
    main()
