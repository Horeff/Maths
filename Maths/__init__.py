__version__ = 1.0

from Maths import Fonctions_Usuelles,equatio,modelisations

class maths():
  def __init__(self):
    self.func = Fonctions_Usuelles.fonction
    self.slve = equatio.equations
    self.mod = modelisations.mode

Maths = maths()
