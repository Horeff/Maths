import numpy as np

class func():
    def lin(self, x , a, b):
        return a * x + b

    def exp(self, x, a, b, c):
        return a * np.exp(x * b) + c

    def sin(self, x, a, b, c, d):
        return a * np.cos(b * x + c) + d

    def pol(self, x, a, b, c):
        return a*x**2 + b * x + c

    def pol2(self, x, a, b, c, d):
        return a * x**3 + b * x**2 + c * x + d

    def pol3(self, x, a, b, c, d, e):
        return a * x ** 4 + b * x ** 3 + c * x**2 + d * x + e

functions = func()