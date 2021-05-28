from main import grad
from buscaarmijo import armijo
from numpy import dot

def bfgs(xk, x, yk, y, hk):
    p = []
    pt = [[],[]]
    q = []
    qt = [[],[]]

    p = x - xk, y - yk
    pt[0].append(x - xk)
    pt[1].append(y - yk)
    q.append(grad(x,y)[0] - grad(xk,yk)[0])
    q.append(grad(x,y)[1] - grad(xk,yk)[1])
    qt[0].append(grad(x,y)[0] - grad(xk,yk)[0])
    qt[1].append(grad(x,y)[1] - grad(xk,yk)[1])

    #h = hk + (1+a/b)*(c/d)-(e+f)/g
    a = dot(qt,dot(hk,q)) #a/b
    b = dot(pt,q)
    
    c = dot(p,pt) #c/d
    d = dot(pt,q)

    e = dot(dot(p,qt),hk) #(e+f)/g
    f = dot(dot(hk,q),pt)
    g = dot(pt,q)

    print (xk,x,yk,y,hk)
    print (p)
    print (pt)
    print (q)
    print (qt)
    print (a)





def quasenewton(x,y):
    d = []
    k = 0
    h = [[1,0],[0,1]]
    xk = 0
    yk = 0

    gradx = grad(x,y)[0]
    grady = grad(x,y)[1]
   
    while not (gradx < 0.00000001 and grady < 0.00000001):
        gradx = grad(x,y)[0]
        grady = grad(x,y)[1]

        a = (-1 * h[0][0] * gradx) + (-1 * h[0][1] * grady)
        b = (-1 * h[1][0] * gradx) + (-1 * h[1][1] * grady)
        d = a, b

        t = armijo(x,y,d)
        xk += x
        yk += y
        x = x + t*d[0]
        y = y + t*d[1]

        h = bfgs(xk,x,yk,y,h)
        break
        k += 1
        if k == 1000:
            break
    return x,y,k

quasenewton(50,15)