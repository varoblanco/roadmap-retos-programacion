#Recursividad - Cuenta atrás
#Numero de casos
n = 100

def imprimir(n):
    if n == 0:
        print(n)
        
    else:
        print(n)
        imprimir(n-1)

#imprimir (n)

#Recursividad - Factorial

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Generar factorial de: "))
resultado = factorial(n)
print(f"El factorial de {n} es {resultado}")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1   
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Generar posición Fibonacci de: "))
resultado = fibonacci(n-1)
print(f"La posicion {n} en la serie Fibonacci es {resultado}")