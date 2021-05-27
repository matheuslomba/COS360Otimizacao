from numpy import exp, log as ln
from math import isnan, pow

def f(x, y):
    funcao = 3**(1/(x+y)) + x**2 + y**2
    return funcao

def grad( x, y ):
    grad_x = 2*x - ( ln(3) * exp(1)**(ln(3)/(x+y)) ) / (x+y)**2
    grad_y = 2*y - ( ln(3) * exp(1)**(ln(3)/(x+y)) ) / (x+y)**2
    gradiente = []
    gradiente.append(grad_x)
    gradiente.append(grad_y)
    return gradiente

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