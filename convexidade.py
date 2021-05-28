from main import hes
from numpy import arange, linalg
from math import isnan

def convexo():
    t = 0.0
    x = 0.0
    y = 0.0
    while t <= 1:
        for x in arange(0.0,100.0, 0.1):
            for y in arange(0.0,100.0,0.1):
                hessiana = hes(x, y)
                if isnan(hessiana[0][0]): #caso em que x = -y ou vice versa e, portanto, o cálculo da hessiana terá divisão por 0, indicando um ponto de descontinuidade da função.
                    return "O gráfico é não convexo e não côncavo."
                elif hessiana[0][1] == hessiana[1][0]: #matriz simétrica
                    autovalores = linalg.eigvals(hessiana)
                    if autovalores[0] < 0 and autovalores[1] < 0: #encontrar autovalores
                        print ("autovalores")
                        return "O gráfico não é convexo."
        t += 0.1
    return "O gráfico é convexo."

print (convexo())