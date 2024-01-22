from Operators.BinaryOperators.BinaryOperator import BinaryOperator


class Plus(BinaryOperator):  # '+'
    def __init__(self, kdimut: float, op_type: int) -> None:
        self._kdimut = kdimut
        self._op_type = op_type  # 1 Binary, 2 Left To Operand Unary , 3 Right To Operand Unary

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        """
        adds two numbers
        :param first_operand: the first operand
        :param second_operand: the second operand
        :return: the sum of the operands
        """
        self.validate_operands(first_operand, second_operand)
        try:
            return first_operand + second_operand
        except OverflowError:
            print("result of + is too damn large!")
            exit()

    def validate_operands(self, first_operand: float, second_operand: float) -> None:
        """
        checks if both operands are valid operands for this class calculation
        :param first_operand: the first operand
        :param second_operand: the second operand
        :return: None
        """
        try:
            float(first_operand)
            float(second_operand)
        except (TypeError, ValueError):
            print("+ didn't get two valid operands")
            exit()
