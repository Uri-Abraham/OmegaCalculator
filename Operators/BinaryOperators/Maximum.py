from Operators.BinaryOperators.BinaryOperator import BinaryOperator


class Max(BinaryOperator):  # '$'
    def __init__(self, kdimut: float, op_type: int) -> None:
        self._kdimut = kdimut
        self._op_type = op_type  # 1 Binary, 2 Left To Operand Unary , 3 Right To Operand Unary

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        self.validate_operands(first_operand, second_operand)
        if first_operand > second_operand:
            return first_operand
        return second_operand

    def validate_operands(self, first_operand: float, second_operand: float) -> None:
        try:
            float(first_operand)
            float(second_operand)
        except (TypeError, ValueError):
            print("$ didn't get two valid operands")
            exit()
