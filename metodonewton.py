from buscaarmijo import armijo
from main import grad, hes, inversa, f

def metnewton(x,y):
    d = []
    k = 0
    count = 0
    callarmijo = 0
    t = 1
    gradx = grad(x,y)[0]
    grady = grad(x,y)[1]
   
    while gradx != 0 and grady != 0:
        gradx = grad(x,y)[0]
        grady = grad(x,y)[1]
       
        hessi = hes(x,y)
        inver = inversa(hessi)
       
        a = (-inver[0][0]) * gradx + (-inver[0][1]) * grady
        b = (-inver[1][0]) * gradx + (-inver[1][1]) * grady
        d = a, b
        t, count = armijo(x,y,d,t)
        callarmijo += count
        x = x + t*d[0]
        y = y + t*d[1]
        k += 1
        if k == 100:
            break
        elif (abs(gradx) < 0.00000001 and abs(grady) < 0.00000001):
            break
    return k,callarmijo,x,y,f(x,y)

print (metnewton(10,10))