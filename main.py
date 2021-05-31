from numpy import exp, log as ln, sqrt

def f(x, y):
    funcao = 3**(1/(x+y)) + x**2 + y**2
    return funcao

def grad( x, y ):
    gradx = 2*x - ((ln(3) * (exp(1)**(ln(3)/(x+y))) / (x+y)**2 ))
    grady = 2*y - ((ln(3) * (exp(1)**(ln(3)/(x+y))) / (x+y)**2 ))
    mgrad = []
    mgrad.append(gradx)
    mgrad.append(grady)
    return mgrad

def grad_d(x,y,d):
    a = grad(x,y)[0] * d[0]
    b = grad(x,y)[1] * d[1]
    soma = a + b
    return soma

def modulograd(x,y):
    mod = sqrt( (grad(x,y)[0])**2 + (grad(x,y)[1])**2 )
    return mod

def hes(x, y):
    hes_xx = 2 - (ln(3) * ( -ln(3) * exp(1)**(ln(3))/(x+y)) - 2 * (x+y) * exp(1)**(ln(3)/(x+y) ) )/(x+y)**4
    hes_xy = -1 * (ln(3) * ( -ln(3) * exp(1)**(ln(3))/(x+y)) - 2 * (x+y) * exp(1)**(ln(3)/(x+y) ) )/(x+y)**4
    hes_yx = -1 * (ln(3) * ( -ln(3) * exp(1)**(ln(3))/(x+y)) - 2 * (x+y) * exp(1)**(ln(3)/(x+y) ) )/(x+y)**4
    hes_yy = 2 - (ln(3) * ( -ln(3) * exp(1)**(ln(3))/(x+y)) - 2 * (x+y) * exp(1)**(ln(3)/(x+y) ) )/(x+y)**4
    hessiana = [[],[]]
    hessiana[0].append(hes_xx)
    hessiana[0].append(hes_xy)
    hessiana[1].append(hes_yx)
    hessiana[1].append(hes_yy)
    return hessiana

def determinante(matriz):
    linhax = matriz[0]
    linhax2 = matriz[1]
    c = linhax[0] * linhax2[1]
    d = linhax[1] * linhax2[0]
    resultado = c - d
    return resultado
 
def inversa(matriz):
    if len(matriz) == 1:
        resultado = [1/(matriz[0])]
        return resultado
    else:
        a = determinante(matriz)
        resultado = [[],[]]
        resultado[0].append((1/a)*matriz[1][1])
        resultado[0].append((1/a)*(-matriz[0][1]))
        resultado[1].append((1/a)*(-matriz[1][0]))
        resultado[1].append((1/a)*matriz[0][0])
    return resultado