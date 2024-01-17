import math


class Operator(object):

    def __init__(self, kdimut: float, op_type: int) -> None:
        self._kdimut = kdimut
        self._op_type = op_type  # 1 Binary, 2 Left To Operand Unary , 3 Right To Operand Unary

    def get_kdimut(self):
        return self._kdimut

    def get_op_type(self):
        return self._op_type

    def binary_operation(self, first_operand: float, second_operand: float):
        pass

    def unary_operation(self, operand: float):
        pass


class Plus(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        return first_operand + second_operand


class Minus(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        return first_operand - second_operand


class Mul(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        return first_operand * second_operand


class Div(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        try:
            return first_operand / second_operand
        except ZeroDivisionError as e:
            print("Division by zero!")
            exit()


class Pow(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        return math.pow(first_operand, second_operand)


class Avg(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        return (first_operand + second_operand) / 2


class Max(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        if first_operand > second_operand:
            return first_operand
        return second_operand


class Min(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        if first_operand > second_operand:
            return second_operand
        return first_operand


class Modulo(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def binary_operation(self, first_operand: float, second_operand: float) -> float:
        return first_operand % second_operand


class Tilda(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def unary_operation(self, operand: float) -> float:
        return -operand


class Factorial(Operator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        super().__init__(kdimut, op_type)

    def unary_operation(self, operand: float) -> int:
        try:
            operand = int(operand)
        except Exception as e:
            print(e)
            exit()
        return Factorial.factorial(operand)

    @staticmethod
    def factorial(num: int) -> int:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return fact