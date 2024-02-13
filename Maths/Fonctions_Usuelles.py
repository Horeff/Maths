import matplotlib.pyplot as plt
import time
import math
import sympy as sp
import importlib
import os

"""
expressions (param e) :
[str]
conv : 
/ = diviser
* = multiplier
+ = additionner
- = soustraire
() = parenthèses de priorité
x = sp.Symbol("x")
y = sp.Symbol("y")
"""

class fonction():
  def __init__(self, e, name):
    try:
      self.e = sp.simplify(e)
    except:
      self.e = e
    self.x = sp.Symbol("x")
    self.y = sp.Symbol("y")
    self.name = name
    try:
      self.der = sp.diff(self.e, self.x)
    except:
      self.der = None
    try:
      self.int = sp.integrate(self.e, self.x)
    except : 
      self.int = None
    try:
      self.inv = sp.solve(self.e - self.y, self.x, dict = True)
      self.inv = sp.simplify(self.inv[-1][self.x])
    except:
      self.inv = None
    try:
      self.limpinf = sp.limit(self.e, self.x, "+oo")
    except:
      self.limpinf = None
    try:
      self.limminf = sp.limit(self.e, self.x, "-oo")
    except:
      self.limminf = None
    try:
      fig = self.show()
      print(fig)
      fig.savefig("generation_mpl_save_to_send.png")
      self.rep = "generation_mpl_save_to_send.png"
    except:
      self.rep = None

  def img(self, ant):
    return self.e.subs(self.x, ant)

  def ant(self, img):
    return self.inv.subs(self.y, img)

  def limit(self, tend):
    return sp.limit(self.e, self.x, tend)
  
  def sub(self,var,expr):
    return self.e.subs(var,sp.simplify(expr))

  def show(self):
    return sp.plot(self.e,(self.x,-6,6), title=f"Courbe de f(x) = ${sp.latex(self.e)}$", show=False)
