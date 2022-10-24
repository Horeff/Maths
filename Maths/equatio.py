import matplotlib.pyplot as plt
import time
import math
import sympy as sp
import importlib
import os

class equations():
  def __init__(self,e,name):
    self.name = name
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    z = sp.Symbol("z")
    self.var = [x,y,z]
    self.var = [i for i in self.var if str(i) in "".join(e)]
    if type(e) == list:
      self.e = [sp.simplify(i) for i in e]
      try:
        self.solutions = sp.linsolve(self.e,self.var)
      except:
        self.solutions = sp.nonlinsolve(self.e,self.var)
    else:
      equa = e.split("=")
      try:
        self.e = sp.Eq(sp.simplify(equa[0]),sp.simplify(equa[1]))
        self.solutions = sp.solve(self.e,self.var)
      except:
        self.e = sp.Eq(sp.simplify(e),0)
        self.solutions = sp.solve(self.e,self.var)

