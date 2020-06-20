class Graph():
  def __init__(self):
    self.operations = []
    self.placeholders = []
    self.variables = []
    self.constants = []

  def as_default(self):
    _default_graph = self
    
_default_graph = Graph()
