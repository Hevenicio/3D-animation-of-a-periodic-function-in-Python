import matplotlib.animation as animation
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import numpy as np

#Criando uma função periodica
def PS(x, y, t):
    return np.sin(y**2 + t) + np.cos(x**2 + t)

#Dados para aplicar na função 
x = np.linspace(-np.pi, np.pi, 101)
y = np.linspace(-np.pi, np.pi, 101)
t = np.linspace(0, 20, 101)

#Cria matrizes de coordenadas a partir das coords x e y
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize = (12, 6), dpi = 100)     
ax = fig.gca(projection = '3d')

#Esta função é chamada periodicamente a partir da FuncAnimation
def update(i):
    Z = PS(X, Y, t[i])
    ax.clear()
    ax.plot_surface(X, Y, Z, cmap = mpl.cm.viridis)
    plt.title(str(i))
    plt.xlabel('$X$', color = 'g')
    plt.ylabel('$Y$', color = 'g')

#Plotagem para chamar a função update() periodicamente
ani = animation.FuncAnimation(fig, update, np.arange(100), interval = 10, repeat = False)

plt.show()