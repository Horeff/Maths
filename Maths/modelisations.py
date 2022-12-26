import numpy as np
from scipy import stats as sp
from Algorithmique import fig
from matplotlib import pyplot as plt
from scipy import optimize
from Maths.Functions import functions
from inspect import getmembers, ismethod

class model():
    def __init__(self, functions):
        self.functions = functions

    def circlefit(self, x, y):
        """
        :param x: abscisses de tous les points
        :param y: ordonnées de tous les points
        :return: coordonnées du centre, rayon, indications sur la validité de la modélisation :
        Le test de Kolmogorov Smirnov, ainsi qu'un coefficient de correlation.
        """
        cx = 0
        cy = 0
        flag = True
        counter = 1
        distances = []
        while flag:
            distances = [np.sqrt((x[i] - cx) ** 2 + (y[i] - cy) ** 2) for i in range(len(x))]
            cx += (x[distances.index(max(distances))] - cx) / (10 / max(distances))
            cy += (y[distances.index(max(distances))] - cy) / (10 / max(distances))
            counter += 1
            j = 1
            perc = 0.05 + counter / 100000
            for i in distances:
                if i + perc * i < np.mean(distances) or i - perc * i > np.mean(distances):
                    break
                j += 1
                if j == len(distances):
                    flag = False
        xp, yp = fig.circle((cx, cy), a=2*np.pi, r=np.mean(distances), resolution=len(x)-1)
        coef = self.Coef_correl((x, y), (xp, yp))
        b, kol = self.Kol_Smir((x, y), (xp, yp))
        return (cx, cy), np.mean(distances), (b, kol, coef)

    def Coef_correl(self, X, Y):
        # Calculer le coefficient de correlation:
        list_x = X[1]
        indexx = X[0]
        list_y = Y[1]
        indexy = Y[0]
        if len(indexx) < len(indexy):
            list_y = list_y[:len(indexx)]
        elif len(indexx) > len(indexy):
            list_x = list_x[:len(indexy)]
        x_Moy = sum(list_x) / len(list_x)
        y_Moy = sum(list_y) / len(list_y)
        dist = []
        den = []
        for i in range(len(list_x)):
            dist.append((list_x[i] - x_Moy) * (list_y[i] - y_Moy))
        for i in range(len(list_x)):
            den.append(np.sqrt((list_x[i] - x_Moy) ** 2 * (list_y[i] - y_Moy) ** 2))
        r = sum(dist) / sum(den)
        return r

    def Kol_Smir(self, X, Y):
        """Idéalement, stat doit tendre vers 0 et pvalue vers 1.
        Pour accepter l'hypothèse que les deux modèles se ressemblent,
        on peut accepter une pvalue de 41% minimum, ou plus si on veut
        une meilleure précision. Dans le cas de déterminer quel modèle
        correspond le mieux au cours, il suffit de prendre la pvalue
        la plus élevée."""
        data_x = X[1]
        data_y = Y[1]
        res = sp.ks_2samp(data_x, data_y)
        if res[1] < 0.05:
            return False, res
        else:
            return True, res

    def parties(self, n, liste = [[]], j = 0):
        l = liste
        if j == n-1:
            l.sort(key = len)
            return l
        else:
            return self.parties(n, liste = l + [i + [j] for i in l], j = j+1)

    def triangle_de_Pascal(self, n):
        liste = [1]
        for i in range(n):
            liste = [1] + [liste[j]+liste[j-1] for j in range(1, len(liste))] + [1]
        return liste

    def Lagrange(self, x : list, y : list) -> list:
        """
        Utilise le polynôme de Lagrange pour trouver le polynôme de
        plus petit degré correspondant le mieux au jeu de données
        :param x: abscisses
        :param y: ordonnées
        :return: Liste des paramètres du polynôme.
        """
        tab = []
        ls = []
        # [1,2,3] -> [[2,3],[1,3],[1,2]]
        for i in range(len(x)):
            tab.append(x[:i]+x[i+1:])
        weights = []
        # poids : [((1-2)*(1-3))e-1, ((2-1)*(2-3))e-1, ((3-1)*(3-2))e-1]
        for i in range(len(x)):
            weights.append(np.prod([1/(x[i]-tab[i][j]) for j in range(len(tab[i]))]))
        # on trouve les parties : [[],[0],[1],[2],[0,1],[0,2],[1,2],[0,1,2]]
        lst = self.parties(len(tab[0]))
        Pascal = self.triangle_de_Pascal(len(lst[-1]))
        for i in range(len(tab)):
            coefs = []
            # on calcule les coefficients [[a],[b],[a,b]] -> [a,b,ab]
            for j in lst:
                coefs.append(np.prod([-tab[i][h] for h in j]))
            index = 0
            l = []
            for h in range(len(Pascal)):
                l.append(coefs[index:index+Pascal[h]])
                index += Pascal[h]
            ls.append([np.sum(l[h])*weights[i]*y[i] for h in range(len(l))])
        L = []
        for i in range(len(ls[0])):
            k = 0
            for j in range(len(ls)):
                k += ls[j][i]
            L.append(k)
        return L

    def fit(self, x : iter, y : iter, print_tests : bool = False, return_every_modelisation : bool = False):
        L = []
        for func in self.functions.funcs:
            try:
                res = optimize.curve_fit(func, xdata = x, ydata = y)[0]
                Y = [func(i, *res) for i in x]
                coef = self.Coef_correl((x, y), (x, Y))
                kol = self.Kol_Smir((x, y), (x, Y))
                L.append((coef, kol, res, func))
            except:pass
        if print_tests:
            for i in L:
                print(f"tested with {i[-1]} : coef = {i[0]} ; kol = {i[1]}")
        if return_every_modelisation:
            list_acc = []
            max = 0
            for i in range(len(L)):
                if L[i][0] > max:
                    max = L[i][0]
            for i in range(len(L)):
                if L[i][0] > max - 0.001*max:
                    list_acc.append(L[i])
            if print_tests: print(f"got : {list_acc}")
            return list_acc, L
        else:
            max1, max2, ind1, ind2 = 0, 1, None, None
            for i in range(len(L)):
                if L[i][1][1][1] > max1:
                    max1 = L[i][1][1][1]
                    ind1 = i
                if L[i][1][1][0] < max2:
                    max2 = L[i][1][1][0]
                    ind2 = i
            if ind1 == ind2:
                if print_tests: print(f"got : {L[ind1][-1]}")
                return [L[ind1]]
            elif ind1 is not None and ind2 is not None:
                if print_tests: print(f"got : {L[ind1][-1]} and {L[ind2][-1]}")
                return (L[ind1], L[ind2])
            else:return L


class fit_func():
    def __init__(self):
        self.funcs = self.fitting_funcs()
        self.names = self.fitting_funcs_names()
        self.expression = functions.expression

    def fitting_funcs(self):
        g = [a[1] for a in getmembers(functions) if ismethod(a[1]) and a[0] != "__init__"]
        return g
    
    def fitting_funcs_names(self):
        g = [a[0] for a in getmembers(functions) if ismethod(a[1]) and a[0] != "__init__"]
        return g


mode = model(fit_func())
