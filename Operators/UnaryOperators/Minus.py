from Operators.UnaryOperators.UnaryOperator import UnaryOperator


class Minus(UnaryOperator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        self._kdimut = kdimut
        self._op_type = op_type  # 1 Binary, 2 Left To Operand Unary , 3 Right To Operand Unary

    def unary_operation(self, operand: float) -> float:
        if self.validate_operand(operand):
            return operand*-1

    def validate_operand(self, operand: float) -> bool:
        try:
            float(operand)
        except (TypeError, ValueError):
            print("Missing an operand")
            exit()
        return True
