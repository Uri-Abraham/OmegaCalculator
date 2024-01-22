from Operators.Operator import Operator


class BinaryOperator(Operator):
    """
    the super class of the binary operators
    """

    def binary_operation(self, first_operand: float, second_operand: float):
        pass

    def validate_operands(self, first_operand: float, second_operand: float):
        pass
