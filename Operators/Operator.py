class Operator(object):
    """
    the super class of all the operators
    """

    def get_kdimut(self):
        """
        :return: the kdimut of the operator
        """
        return self._kdimut

    def get_op_type(self):
        """
        :return: the operator's kdimut
        """
        return self._op_type

