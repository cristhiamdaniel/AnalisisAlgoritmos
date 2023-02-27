'''
Implementación de la Función de Collatz.

Procedure collatz(integer n) 
    counter = 0
    while(n =! 1) 
        if (n mod 2= 0) then //Se verifica si n es número par. 
            n=n/2 
        else 
            n=3*n+1 
        end-of-if 
        counter = counter + 1 
    end-of-while 
    return counter 
end-of-procedure

'''

def collatz(n):
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(counter)
        counter = counter + 1
    return counter

# Funcion Principal

def main():
    n = int(input("Ingrese un numero entero: "))
    print("El numero de pasos para llegar a 1 es", collatz(n))

if __name__ == "__main__":
    main()

