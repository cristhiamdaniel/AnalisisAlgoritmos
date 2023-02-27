import math

'''
Programa Algoritmo Correcto e Incorrecto
'''

# Algoritmo Correcto del Factorial

def factorialCorrecto(n):
    if n == 0:
        return 1
    else:
        return n * factorialCorrecto(n-1)

# Algoritmo Incorrecto del Factorial (Aproximacion de Stirling)
'''
Procedure factorial(integer n) 
    // ln denota a la función logaritmo natural. 
    // pow(b, x) calcula bx. 
    return pow(2.7182, 0.5 * ln(2 * 3.1416) + (0.5 + n) * ln(n) - n) 
end-of-procedure
'''

def factorialIncorrecto(n):
    return 2.7182 ** (0.5 * math.log(2 * 3.1416) + (0.5 + n) * math.log(n) - n)

# Funcion Principal

def main():
    n = int(input("Ingrese un numero entero: "))
    print("El factorial de", n, "es", factorialCorrecto(n))
    print("El factorial de", n, "es", factorialIncorrecto(n))

if __name__ == "__main__":
    main()