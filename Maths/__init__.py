from packages import Fonctions_Usuelles, Wolf_alpha

Wolf_alpha.ask("e^x/(1-e^x)")
#g = Fonctions_Usuelles.fonction([1,2,3,4,5],[1,2,3,4,5], "", "test")
#g.modeliser()
g = Fonctions_Usuelles.fonction("exp(x)/(1-exp(x))","test")
g.show()

class maths():
  def __init__(self):
    self.func = Fonctions_Usuelles.fonction

  

Maths = maths()
