from sympy import *

"""
Programa que calcula la expansion binomial de un binomio y
el termino i-esimo de la expansion binomial de un binomio
"""

# Definimos las variables simbolicas
x = Symbol('x')
y = Symbol('y')


def factorial(n):
    """
    Funcion que calcula el factorial de un numero entero
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def binomial(n, k):
    """
    Funcion que calcula el coeficiente binomial
    """
    return factorial(n) / (factorial(k) * factorial(n - k))


def expansion_binomial(a, b, n):
    """
    Funcion que calcula la expansion binomial de un binomio
    """
    resultado = 0
    for k in range(n + 1):
        resultado += binomial(n, k) * (a * x) ** (n - k) * (b * y) ** k
    return resultado


def termino_binomial(a, b, n, i):
    """
    Funcion que calcula el termino i-esimo de la expansion binomial de un binomio
    """
    return binomial(n, i) * (a * x) ** (n - i) * (b * y) ** i


# Ejemplo
print(expansion_binomial(1, 1, 3))
print(termino_binomial(1, 1, 3, 2))
