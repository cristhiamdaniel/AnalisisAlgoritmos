import matplotlib.pyplot as plt
import numpy as np

# Definir las funciones f(n) y g(n)
def f(n):
    return 2 ** (n + 1)

def g(n):
    return 2 ** n

# Definir los valores de c1, c2 y n0 que satisfacen la definición de Theta
c1 = 1
c2 = 3
n0 = 1

# Crear una lista de valores de n para graficar
n_values = np.arange(0, 10)

# Crear una figura para la gráfica
fig, ax = plt.subplots()

# Graficar las funciones f(n), c1*g(n) y c2*g(n)
ax.plot(n_values, f(n_values), label="f(n)")
ax.plot(n_values, c1 * g(n_values), label="c1 * g(n)")
ax.plot(n_values, c2 * g(n_values), label="c2 * g(n)")

# Graficar la línea vertical punteada que indica n0
ax.axvline(n0, color="gray", linestyle="dashed")

# Agregar una leyenda y un título a la gráfica
ax.legend()
ax.set_title("Gráfica de f(n), c1*g(n) y c2*g(n)")

# Mostrar la gráfica
plt.show()
