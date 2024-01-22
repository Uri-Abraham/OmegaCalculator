import sys

from Operators.UnaryOperators.UnaryOperator import UnaryOperator


class Factorial(UnaryOperator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        self._kdimut = kdimut
        self._op_type = op_type  # 1 Binary, 2 Left To Operand Unary , 3 Right To Operand Unary

    def unary_operation(self, operand: float) -> int:
        """
        calculate the factorial of the operand
        :param operand: the operand
        :return: the result of the factorial
        """
        if self.validate_operand(operand):
            return Factorial.factorial(int(operand))
        else:
            print("Can't execute factorial on a non-natural number")
            exit()

    @staticmethod
    def factorial(num: int) -> int:
        """
        calculates a factorial for a given number
        :param num: a natural number
        :return: the result of the factorial
        """
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        if fact > 1.7976931348623157e+308:  # max size of float
            print("Result of factorial is too large!!")
            exit()
        return fact

    def validate_operand(self, operand: float) -> bool:
        """
        checks if the operand is a valid operand for this class calculation
        :param operand: the operand
        :return: true if the operand is valid
        """
        try:
            float(operand)
        except (TypeError, ValueError):
            print("Missing an operand on factorial")
            exit()

        if operand < 0 or operand % 1 != 0:
            return False
        return True
