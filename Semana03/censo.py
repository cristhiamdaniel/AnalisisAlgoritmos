"""
Se tiene un censo de 5000000 registros.
cada registro tiene la siguiente estructura:
numero de identificacion - nombre - edad - impuestos
Los numeros de identificacion están ordenados ascendentemente y crecen de manera aleatoria en 1 o 2 unidades.
El nombre corresponde a una cadena de 5 caracteres del alfabeto tomados de manera aleatoria.
La edad es un numero aleatorio dentro de un rango de 18 a 99.
El impuesto es un bool que se toma aleatoriamente de la lista: True, True, True, False.

Crear un menu para realizar busquedas por numero y por nombre y mostrar en pantalla el resultado.

Una vez validado el programa.
Realizar la comparacion de complejidad entre ambas funciones a traves de una grafica en donde los datos de entrada (censos) incremente en un factor de 5:
500_000
2_500_000
12_500_000
62_500_000
312_500_000
...
"""

import random
import time
import pandas as pd
import matplotlib.pyplot as plt

class Censo:
    def __init__(self, tamano):
        self.censo = []
        self.alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.numero = 0
        self.tamano = tamano # numero de registros

    def crear_censo(self):
        for i in range(self.tamano):
            aumento = random.randint(1, 2)
            self.numero += aumento

            letras = random.sample(self.alfabeto, 5)
            nombre = "".join(letras)

            edad = random.randint(18, 99)

            impuestos = random.choice((True, True, True, False))

            self.censo.append([self.numero, nombre, edad, impuestos])

            if len(self.censo) % 100000 == 0:
                print("Creados", len(self.censo), "registros")

        print("Censo creado.")
        print("ultimo registro: ", self.censo[-1])

    def busqueda_numero(self, numero):
      # Busqueda binario
        inicio = 0
        final = len(self.censo) - 1

        while inicio <= final:
            medio = (inicio + final) // 2
            if self.censo[medio][0] == numero:
                return medio
            elif numero < self.censo[medio][0]:
                final = medio - 1
            else:
                inicio = medio + 1

        return None

    def busqueda_nombre(self, nombre):
      # busqueda secuencial
        for i in range(len(self.censo)):
            if self.censo[i][1] == nombre:
                return i
        return None

    def mostrar_registro(self, indice):
        print("Registro encontrado:")
        print("Numero:", self.censo[indice][0])
        print("Nombre:", self.censo[indice][1])
        print("Edad:", self.censo[indice][2])
        print("Impuestos:", self.censo[indice][3])

    def mostrar_censo(self):
        print("ultimo registro: ", self.censo[-1])

    def mostrar_tiempos(self, tiempos):
        print("Tiempos de busqueda")
        print("Busqueda por numero:", tiempos[0])
        print("Busqueda por nombre:", tiempos[1])


def main():
    #tiempos = []
  """
    for i in range(5):
        tamano = 500_000 * (i + 1)
        censo = Censo(tamano)
        censo.crear_censo()
        inicio = time.perf_counter()
        censo.busqueda_numero(0)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        inicio = time.perf_counter()
        censo.busqueda_nombre("ABCDEAAAA")
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        censo.mostrar_tiempos(tiempos)

    print("Tiempos de busqueda")
    print("Busqueda por numero:", tiempos[0])
    print("Busqueda por nombre:", tiempos[1])
  """
  tamano = 500_000
  censo = Censo(tamano)
  censo.crear_censo()

main()
