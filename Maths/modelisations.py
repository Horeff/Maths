import numpy as np

class model():
  def __init__(self):
    pass
  
  def circlefit(self,x,y):
    cx = 0
    cy = 0
    flag = True
    counter = 1
    while flag:
        distances = [np.sqrt((x[i]-cx)**2+(y[i]-cy)**2) for i in range(len(x))]
        cx += (x[distances.index(max(distances))]-cx)/(10/max(distances))
        cy += (y[distances.index(max(distances))]-cy)/(10/max(distances))
        counter += 1
        j = 1
        perc = 0.05+counter/100000
        for i in distances:
            if i+perc*i < np.mean(distances) or i-perc*i > np.mean(distances):
                break
            j += 1
            if j == len(distances):
                flag = False
    return (cx,cy),np.mean(distances)

mode = model()
