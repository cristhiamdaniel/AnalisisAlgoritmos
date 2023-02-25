from sympy import Symbol, expand, binomial

def expansion_binomial(a, b, n):
    x = Symbol('x')
    y = Symbol('y')
    resultado = ""
    for i in range(n + 1):
        coeficiente = binomial(n, i)
        termino = coeficiente
        if i == 0:
            termino *= (a ** n)
        elif i == n:
            termino *= (b ** n)
        else:
            termino *= (a ** (n - i)) * (b ** i)
        resultado += str(termino * x ** (n - i) * y ** i) + " + "
    return resultado[:-3]

# Ejemplo de uso
from sympy import pi, E
a = 2
b = 3
n = 3
resultado = expand(expansion_binomial(a, b, n)).subs({Symbol('x'): pi, Symbol('y'): E})
print(resultado)
