from Operators.UnaryOperators.UnaryOperator import UnaryOperator


class Hashtag(UnaryOperator):
    def __init__(self, kdimut: float, op_type: int) -> None:
        self._kdimut = kdimut
        self._op_type = op_type  # 1 Binary, 2 Left To Operand Unary , 3 Right To Operand Unary

    def unary_operation(self, operand: float) -> int:
        sum_of_digits = 0
        if self.validate_operand(operand):
            operand_str = str(operand)
            for i in range(len(operand_str)):
                if operand_str[i].isdigit():
                    sum_of_digits += int(operand_str[i])
        return sum_of_digits

    def validate_operand(self, operand: float) -> bool:
        try:
            float(operand)
        except (TypeError, ValueError) as e:
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
