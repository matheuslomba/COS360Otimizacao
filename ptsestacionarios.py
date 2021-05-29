from main import grad
from numpy import arange

def estacionario():
    for x in arange(-10.0,10.0,0.1):
        for y in arange(-10.0,10.0,0.1):
            if x+y == 0:
                continue
            else:
                g = grad(x,y)
                if g[0] > -0.5 and g[0] < 0.5 and g[1] > -0.5 and g[1] < 0.5:
                    print("x,y: ", x, " , ", y)
                    print("gradiente(x,y): ",g)
                    print("-------------")
    return 0

estacionario()