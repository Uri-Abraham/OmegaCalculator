from Operators.UnaryOperators.UnaryOperator import UnaryOperator


class Factorial(UnaryOperator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        self._kdimut = kdimut
        self._op_type = op_type  # 1 Binary, 2 Left To Operand Unary , 3 Right To Operand Unary

    def unary_operation(self, operand: float) -> int:
        if self.validate_operand(operand):
            return Factorial.factorial(int(operand))

    @staticmethod
    def factorial(num: int) -> int:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return fact

    def validate_operand(self, operand: float):
        try:
            operand = int(operand)
        except Exception as e:
            print(e)
            exit()
