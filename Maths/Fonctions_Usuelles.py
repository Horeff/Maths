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
    sp.init_printing()
    try:
      self.e = sp.simplify(e)
    except:
      self.e = e
    self.x = sp.Symbol("x")
    self.y = sp.Symbol("y")
    self.name = name
    try:
      self.der = sp.latex(sp.diff(self.e, self.x))
    except:
      self.der = None
    try:
      self.int = sp.latex(sp.integrate(self.e, self.x))
    except : 
      self.int = None
    print(self.int)
    try:
      self.inv = sp.solve(self.e - self.y, self.x, dict = True)
      self.inv = sp.latex(sp.simplify(self.inv[-1][self.x]))
    except:
      self.inv = None
    try:
      self.limpinf = sp.latex(sp.limit(self.e, self.x, "+oo"))
    except:
      self.limpinf = None
    try:
      self.limminf = sp.latex(sp.limit(self.e, self.x, "-oo"))
    except:
      self.limminf = None
    try:
      fig=plt.figure()
      plt.ion()
      self.show()
      plt.close(fig)
      plt.savefig("generation_mpl_save_to_send.png")
      self.rep = "generation_mpl_save_to_send.png"
    except:
      self.rep = None

  def img(self, ant):
    return self.e.subs(self.x, ant)

  def ant(self, img):
    return self.inv.subs(self.y, img)

  def limit(self, tend):
    return sp.limit(self.e, self.x, tend)

  def show(self):
    sp.plot(self.e,(self.x,-6,6), title=f"Courbe de f(x) = ${sp.latex(self.e)}$")
