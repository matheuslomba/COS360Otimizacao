from numpy import exp,log as ln

def f(x, y):
    funcao = 3**(1/(x+y)) + x**2 + y**2
    return funcao

def gradiente( x, y ):
    gradx = 2*x - ((ln(3) * (exp(1)**(ln(3)/(x+y))) / (x+y)**2 ))
    grady = 2*y - ((ln(3) * (exp(1)**(ln(3)/(x+y))) / (x+y)**2 ))
    mgrad= []
    mgrad+= [gradx]
    mgrad+= [grady]
    return mgrad
 
def grad_d(x,y,d):
    a=gradiente(x,y)[0]*d[0]
    b=gradiente(x,y)[1]*d[1]
    soma=a+b
    return soma

def auxarmijo(x,y,t,d):
    a=x+t*d[0]
    b=y+t*d[1]
    return f(a,b)

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
    linhax=matriz[0]
    linhax2=matriz[1]
    c= linhax[0]*linhax2[1]
    d= linhax[1]*linhax2[0]
    resultado= c-d
    return resultado

def inversa(matriz):
    a=determinante(matriz)
    resultado=[[],[]]
    resultado[0].append((1/a)*matriz[1][1])
    resultado[0].append((1/a)*(-matriz[0][1]))
    resultado[1].append((1/a)*(-matriz[1][0]))
    resultado[1].append((1/a)*matriz[0][0])
    return resultado






def armijo(x,y,d,t):
    gamma=0.8
    N=1/2
    count=0
    while auxarmijo(x,y,t,d)>f(x,y)+N*t*grad_d(x,y,d):
        t=gamma*t
        count+=1
    return t


def metgradiente(x,y):
    d=[]
    k=0
    gradx=gradiente(x,y)[0]
    grady=gradiente(x,y)[1]
    t=1
    while not(abs(gradx)<0.00000001 and abs(grady)<0.00000001):
        gradx=gradiente(x,y)[0]
        grady=gradiente(x,y)[1]
        d = -gradx,-grady
       
        t=armijo(x,y,d,t)
         
        x=x+t*d[0]
        y=y+t*d[1]
        k+=1
        if k==100:
            break
    print(modgrad(gradx,grady))
    return x,y

def metnewton(x,y):
    d=[]
    k=0
    t=1
    gradx=gradiente(x,y)[0]
    grady=gradiente(x,y)[1]
   
    while not(abs(gradx)<0.00000001 and abs(grady)<0.00000001):
        gradx=gradiente(x,y)[0]
        grady=gradiente(x,y)[1]
       
        hessi=hes(x,y)
        inver=inversa(hessi)
       
       
        a=(-inver[0][0])*gradx+(-inver[0][1])*grady
        b=(-inver[1][0])*gradx+(-inver[1][1])*grady
        d =a,b
        t=armijo(x,y,d,t)
       
        x=x+t*d[0]
        y=y+t*d[1]
        k+=1
        if k==100:
            break
    print(modgrad(gradx,grady))
    print(gradx)
    return x,y



def metquasenewton(x,y):
    d=[]
    k=0
    gradx=gradiente(x,y)[0]
    grady=gradiente(x,y)[1]
    H=[[1,0],[0,1]]
    xk=0
    yk=0
    p=[]
    q=[]
   
    while not(abs(gradx)<0.00000001 and abs(grady)<0.00000001):
        gradx=gradiente(x,y)[0]
        grady=gradiente(x,y)[1]
       
        aa=H[0][0]*gradx+H[0][1]*grady
        bb=H[1][0]*gradx+H[1][1]*grady
        d =-aa,-bb
        t=armijo(x,y,d)
       
        xk=x
        yk=y
        x=x+t*d[0]
        y=y+t*d[1]
       
        px=x-xk
        py=y-yk
        p=px,py
       
        qx=gradiente(x,y)[0]-gradx
        qy=gradiente(x,y)[1]-grady
        q=qx,qy
       
       
        a=multmat_12_22(q,H)
       
        a1=multmat_12_21(a,q)
       
        b=multmat_12_21(p,q)
       
        a2=a1/b
       
       
        c=multmat_21_12(p,p)
        c1=divMultMat_22(c,b,0)
        c2=divMultMat_22(c1,a2,1)
       
        dd=somamat_22(c2,c)
        d1=somamat_22(dd,H)
       
        e=multmat_21_12(p,q)
        e1=multmat_22_22(e,H)
        e2=divMultMat_22(e1,b,0)
       
        f=multmat_22_21(H,q)
        f1=multmat_21_12(f,p)
        f2=divMultMat_22(f1,b,0)
       
        ef=somamat_22(e2,f2)
       
        H=submat_22(d1,ef)
       
        k+=1
        if k==8:
            break
    return x,y


def multmat_12_22(x,y):
    a=x[0]*y[0][0]+x[1]*y[1][0]
    b=x[0]*y[1][0]+x[1]*y[1][1]
    resultado=[a,b]
    return resultado

def multmat_12_21(x,y):
    resultado=x[0]*y[0]+x[1]*y[1]
    return resultado

def multmat_21_12(x,y):

    resultado=[[x[0]*y[0],x[0]*y[1]],[x[1]*y[0],x[1]*y[1]]]
    return resultado

def divMultMat_22(x,y,c):
    if c==0:
        a=x[0][0]/y
        b=x[0][1]/y
        c=x[1][0]/y
        d=x[1][1]/y
        resultado=[[a,b],[c,d]]
    if c==1:
        a=x[0][0]*y
        b=x[0][1]*y
        c=x[1][0]*y
        d=x[1][1]*y
        resultado=[[a,b],[c,d]]
    return resultado

def somamat_22(x,y):
    a=x[0][0]+y[0][0]
    b=x[1][0]+y[1][0]
    c=x[0][1]+y[0][1]
    d=x[1][1]+y[1][1]
    resultado=[[a,b],[c,d]]
    return resultado

def submat_22(x,y):
    a=x[0][0]-y[0][0]
    b=x[1][0]-y[1][0]
    c=x[0][1]-y[0][1]
    d=x[1][1]-y[1][1]
    resultado=[[a,b],[c,d]]
    return resultado

def multmat_22_22(x,y):
    a=x[0][0]*y[0][0]+x[0][1]*y[1][0]
    b=x[0][0]*y[0][1]+x[0][1]*y[1][1]
    c=x[1][0]*y[0][0]+x[1][1]*y[1][0]
    d=x[1][0]*y[0][1]+x[1][1]*y[1][1]
    resultado=[[a,b],[c,d]]
    return resultado

def multmat_22_21(x,y):
    a=x[0][0]*y[0]+x[0][1]*y[1]
    b=x[1][0]*y[0]+x[1][1]*y[1]
    resultado=[a,b]
    return resultado
def modgrad(x,y):
    a=x**2+y**2
    b=a**(0.5)
    return b    
#print(metquasenewton(1,1),"quase newton")
print(metnewton(10,10),"newton")
#print(metgradiente(10,10),"gradiente")