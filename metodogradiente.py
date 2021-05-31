from main import grad, f, modulograd, hes
from buscaarmijo import armijo

def metgrad(x,y):
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
        d = -gradx, -grady
        t, count = armijo(x,y,d,t)
        callarmijo += count
        x = x + t*d[0]
        y = y + t*d[1]
        k += 1
        if k == 100:
            break
        elif (abs(gradx) <= 0.00000001 and abs(grady) <= 0.00000001):
            break
    print ("Iter.: ", k)
    print ("Call Armijo: ", callarmijo)
    print ("Opt. Point: (", x, ",", y, ")")
    print ("Opt Value: ", f(x,y))
    print ("Error: ", modulograd(x,y))
    return 0

print (metgrad(10,10))
print("------------------")
print (metgrad(6,6))
print("------------------")
print (metgrad(0.8,0.8))
print("------------------")
print (metgrad(0.5,0.5))
print("------------------")
print (metgrad(0.3,0.3))
print("------------------")
