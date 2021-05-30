from main import grad
from numpy import arange

#Calcular os pontos críticos da função
    #Caso gradiente da função nos pontos x e y seja 0, printa os pontos x e y
def pts_criticos():
    for x in arange(-10.0,10.0,0.1):
        for y in arange(-10.0,10.0,0.1):
            if x+y == 0:
                continue
            else:
                g = grad(x,y)
                if g[0] > -0.2 and g[0] < 0.2 and g[1] > -0.2 and g[1] < 0.2:
                    print("x,y: ", x, " , ", y)
                    print("gradiente(x,y): ", g)
                    print("-------------")
    return 0

pts_criticos()