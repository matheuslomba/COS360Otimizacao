from main import grad, f
from buscaarmijo import armijo

def metgrad(x,y):
    d = []
    k = 0
    gradx = grad(x,y)[0]
    grady = grad(x,y)[1]
    while not (gradx < 0.00000001 and grady < 0.00000001):
        gradx = grad(x,y)[0]
        grady = grad(x,y)[1]
        d = -gradx, -grady
        t = armijo(x,y,d)
        x = x + t*d[0]
        y = y + t*d[1]
        k += 1
        if k == 100:
            break
    return x,y,k


print (metgrad(5,5))