def coeficiente_binomial(n, k):
    if 0 <= k <= n:
        n_fac = 1
        k_fac = 1
        nk_fac = 1
        for i in range(1, n + 1):
            n_fac *= i
        for i in range(1, k + 1):
            k_fac *= i
        for i in range(1, n - k + 1):
            nk_fac *= i
        return n_fac // (k_fac * nk_fac)
    else:
        return 0

def termino_binomial(a, b, n, i):
    termino = 0
    for k in range(i):
        coeficiente = coeficiente_binomial(n, k)
        termino += coeficiente * (a ** (n - k)) * (b ** k)
    termino *= (a ** (i - n - 1)) * (b ** n)
    return termino

# Ejemplo de uso
a = 2
b = 3
n = 4
i = 3
resultado = termino_binomial(a, b, n, i) # tercer termino de la expansion de (2x + 3y)^4
print(resultado)
