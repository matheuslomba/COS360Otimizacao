from buscaarmijo import armijo
from main import grad, hes, inversa, f

def metnewton(x,y):
    d = []
    k = 0
    gradx = grad(x,y)[0]
    grady = grad(x,y)[1]
   
    while not (gradx < 0.00000001 and grady < 0.00000001):
        gradx = grad(x,y)[0]
        grady = grad(x,y)[1]
       
        hessi = hes(x,y)
        inver = inversa(hessi)
       
        a = (-inver[0][0]) * gradx + (-inver[0][1]) * grady
        b = (-inver[1][0]) * gradx + (-inver[1][1]) * grady
        d = a, b
        t = armijo(x,y,d)
        x = x + t*d[0]
        y = y + t*d[1]
        k += 1
        if k == 1000:
            break
    return x,y,k

print (metnewton(10,5))