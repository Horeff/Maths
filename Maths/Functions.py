import numpy as np

class func():
    def __init__(self):
        self.expressions = {"lin": (["a", "b"], "a * x+b"), "exp": (["a", "b", "c"], "a * exp(x*b) + c"),
                            "sin": (["a", "b", "c", "d"], "a * sin(b*x + c) + d"),
                            "pol": (["a", "b", "c"], "a*x**2 + b*x + c"),
                            "pol3": (["a", "b", "c", "d"], "a*x**3 + b*x**2 + c*x + d"),
                            "pol4": (["a", "b", "c", "d", "e"], "a*x**4 + b*x**3 + c*x**2 + d*x + e")}
    def lin(self, x , a, b):
        return a * x + b

    def exp(self, x, a, b, c):
        return a * np.exp(x * b) + c

    def sin(self, x, a, b, c, d):
        return a * np.cos(b * x + c) + d

    def pol(self, x, a, b, c):
        return a*x**2 + b * x + c

    def pol3(self, x, a, b, c, d):
        return a * x**3 + b * x**2 + c * x + d

    def pol4(self, x, a, b, c, d, e):
        return a * x ** 4 + b * x ** 3 + c * x**2 + d * x + e

functions = func()