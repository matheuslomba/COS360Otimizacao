from main import f, grad_d

def auxarmijo(x,y,t,d):
    a = x + t*d[0]
    b = y + t*d[1]
    return f(a,b)

def armijo(x,y,d):
    gamma = 0.8
    N = 0.5
    t = 1
    count=0
    while auxarmijo(x,y,t,d) > f(x,y) + N*t*grad_d(x,y,d):
        t = gamma * t
        count += 1
    return (t,count)