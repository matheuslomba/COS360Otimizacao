from main import grad, inversa, f
from buscaarmijo import armijo
from numpy import dot

def bfgs(xk, x, yk, y, hk):
    pt = []
    p = [[],[]]
    qt = []
    q = [[],[]]

    pt.append(x - xk)
    pt.append(y - yk)
    p[0].append(x - xk)
    p[1].append(y - yk)
    qt.append(grad(x,y)[0] - grad(xk,yk)[0])
    qt.append(grad(x,y)[1] - grad(xk,yk)[1])
    q[0].append(grad(x,y)[0] - grad(xk,yk)[0])
    q[1].append(grad(x,y)[1] - grad(xk,yk)[1])

    a1 = dot(qt,hk)
    a = dot(a1,q) #a/b = a * b-

    b = [ [p[0][0]*pt[0] , p[0][0]*pt[1]] , [p[1][0]*pt[0] , p[1][0]*pt[1]] ] #c/d = c * d-

    c1 = [ [p[0][0]*qt[0] , p[0][0]*qt[1]] , [p[1][0]*qt[0] , p[1][0]*qt[1]] ] #(e+f)/g = (e+f) * g-
    c = dot(c1,hk)
    d1 = dot(hk,q)
    d = [ [d1[0][0]*pt[0] , d1[0][0]*pt[1]] , [d1[1][0]*pt[0] , d1[1][0]*pt[1]] ]

    e = dot(pt,q)
    ie = inversa(e)

    aie = [dot(a,ie)]
    bie = [ [b[0][0]*ie[0] , b[0][1]*ie[0]] , [b[1][0]*ie[0] , b[1][1]*ie[0]] ]
    cd = [ [c[0][0] + d[0][0] , c[0][1] + d[0][1]] , [c[1][0] + d[1][0] , c[1][1] + d[1][1]] ]
    cdie = [ [cd[0][0]*ie[0] , cd[0][1]*ie[0]] , [cd[1][0]*ie[0] , cd[1][1]*ie[0]] ]

    um_mais_aie = [1 + aie[0]]
    um_mais_aie_x_bie = [ [bie[0][0]*um_mais_aie[0] , bie[0][1]*um_mais_aie[0]] , [bie[1][0]*um_mais_aie[0] , bie[1][1]*um_mais_aie[0]] ]

    um_mais_aie_x_bie_menos_cdie = [[],[]]
    um_mais_aie_x_bie_menos_cdie[0].append(um_mais_aie_x_bie[0][0] - cdie[0][0])
    um_mais_aie_x_bie_menos_cdie[0].append(um_mais_aie_x_bie[0][1] - cdie[0][1])
    um_mais_aie_x_bie_menos_cdie[1].append(um_mais_aie_x_bie[1][0] - cdie[1][0])
    um_mais_aie_x_bie_menos_cdie[1].append(um_mais_aie_x_bie[1][1] - cdie[1][1])

    h = [[],[]]
    h[0].append(hk[0][0] + um_mais_aie_x_bie_menos_cdie[0][0])
    h[0].append(hk[0][1] + um_mais_aie_x_bie_menos_cdie[0][1])
    h[1].append(hk[1][0] + um_mais_aie_x_bie_menos_cdie[1][0])
    h[1].append(hk[1][1] + um_mais_aie_x_bie_menos_cdie[1][1])

    return h


def metquasenewton(x,y):
    d = []
    k = 0
    h = [[1,0],[0,1]]
    xk = 0
    yk = 0

    gradx = grad(x,y)[0]
    grady = grad(x,y)[1]
   
    while not (abs(gradx) < 0.00000001 and abs(grady) < 0.00000001):
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

        k += 1
        if k == 100:
            break
    return x,y,k,f(x,y)

print(metquasenewton(1,1))