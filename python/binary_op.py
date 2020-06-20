from python.op import Operation


class BinaryOperation(Operation):
  def __init__(self, a, b):
    super().__init__([a, b])