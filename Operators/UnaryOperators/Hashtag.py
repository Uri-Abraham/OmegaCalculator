from Operators.UnaryOperators.UnaryOperator import UnaryOperator


class Hashtag(UnaryOperator):  # '#'
    def __init__(self, kdimut: float, op_type: int) -> None:
        self._kdimut = kdimut
        self._op_type = op_type  # 1 Binary, 2 Left To Operand Unary , 3 Right To Operand Unary

    def unary_operation(self, operand: float) -> int:
        """
        calculates the sum of the digits in the operand
        :param operand: the operand
        :return: the sum of the digits
        """
        sum_of_digits = 0
        if self.validate_operand(operand):
            operand_str = str(operand)
            for i in range(len(operand_str)):
                if operand_str[i] == "e":
                    return sum_of_digits
                if operand_str[i].isdigit():
                    sum_of_digits += int(operand_str[i])
        return sum_of_digits

    def validate_operand(self, operand: float) -> bool:
        """
        checks if the operand is a valid operand for this class calculation
        :param operand: the operand
        :return: true if the operand is valid
        """
        try:
            float(operand)
        except (TypeError, ValueError):
            print("Hashtag didn't get operator")
            exit()
        if operand >= 0:
            try:
                str(operand)
            except Exception as e:
                print(e)
                exit()
            return True
        else:
            print("Hashtag can't operate on a negative number!")
            exit()
