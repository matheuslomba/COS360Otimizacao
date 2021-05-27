from main import grad
from numpy import arange

#Calcular os pontos críticos da função
    #Caso gradiente da função nos pontos x e y seja 0, printa os pontos x e y
def pts_criticos():
    x = 0.0
    y = 0.0
    p = 0
    for x in arange(0.0,100.0, 0.1):
        for y in arange(0.0,100.0,0.1):
            if (x+y) == 0.0:
                continue
            else:
                gradiente = grad(x, y)
                if gradiente[0] == 0.0 and gradiente[1] == 0.0:
                    print (f"P({x},{y} é um ponto crítico.")
                    p += 1
    if p == 0:
        print ("Não há pontos críticos para essa função.")

pts_criticos()