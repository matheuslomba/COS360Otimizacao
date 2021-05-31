from  numpy import linspace, meshgrid
from matplotlib.pyplot import figure, axes, show
from main import f

#Plotar gráfico da função f definida acima
x = y = linspace(-100, 100, 500) #determina o tamanho dos eixos (de -100 a 100) e a quantidade de valores entre eles (500)
X, Y = meshgrid(x, y)
Z = f(X,Y)

fig = figure(figsize = (5,4)) #tamanho da imagem em pop-up que aparecerá o gráfico
ax = axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap='prism')

ax.set_title("f(x,y) = 3**(1/(x+y)) + x**2 + y**2", fontsize = 8)
ax.set_xlabel('x', fontsize = 8)
ax.set_ylabel('y', fontsize = 8)
ax.set_zlabel('Z', fontsize = 8)

show()