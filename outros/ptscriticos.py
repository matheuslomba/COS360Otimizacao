from main import grad, f, modulograd
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
                if abs(g[0]) < 10**(-4) and abs(g[1]) < 10**(-4):
                    print("x,y: ", x, " , ", y)
                    print("gradiente(x,y): ", g)
                    print ("f(x,y): ", f(x,y))
                    print ("Error: ", modulograd(x,y))
                    print("-------------")
    return 0

pts_criticos()