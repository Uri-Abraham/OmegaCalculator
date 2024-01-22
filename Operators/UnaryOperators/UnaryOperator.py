from Operators.Operator import Operator


class UnaryOperator(Operator):
    """
    the super class of the binary operators
    """

    def unary_operation(self, operand: float):
        pass

    def validate_operand(self, operand: float):
        pass
