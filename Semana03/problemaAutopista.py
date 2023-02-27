"""
Una empresa de autopistas tiene instalada una camara que cuenta el número de vehículos que pasa por una autopista, y tiene instaladas unas gomas que cuentan el número de ruedas de los vehículos que pasan por la autopista.

La empresa quiere contratar a un programador para que elabore un algoritmo que a partir del número de vehículos y el número de ruedas, extraiga la cantidad de coches y motos que pasan por la autopista

Vehículos = coches + motos
Ruedas = coches * 4 + motos * 2
"""

# Complejidad cuadratica

def algoritmo1(vehiculos, ruedas):
    for coches in range(vehiculos + 1):
        for motos in range(vehiculos + 1):
            if coches + motos == vehiculos and coches * 4 + motos * 2 == ruedas:
                return coches, motos
    return None

# Complejidad lineal

def algoritmo2(vehiculos, ruedas):
    for coches in range(vehiculos + 1):
        motos = vehiculos - coches
        if coches * 4 + motos * 2 == ruedas:
            return coches, motos
    return None

# Complejidad constante

def algoritmo3(vehiculos, ruedas):
    coches = ruedas//2 - vehiculos
    motos = vehiculos - coches

    if coches * 4 + motos * 2 == ruedas:
        return coches, motos
    return None

# Funcion Principal

def main():
    vehiculos = int(input("Ingrese el numero de vehiculos: "))
    ruedas = int(input("Ingrese el numero de ruedas: "))

    print("Algoritmo 1:", algoritmo1(vehiculos, ruedas))
    print("Algoritmo 2:", algoritmo2(vehiculos, ruedas))
    print("Algoritmo 3:", algoritmo3(vehiculos, ruedas))

if __name__ == "__main__":
    main()