"""
Ejercicio

Implementa una estructura de pila (stack) y una de cola (queue) utilizando listas en Python. Realiza las siguientes operaciones para cada estructura:

Parte 1: Pila (LIFO - Last In, First Out)
Crea una pila vacía.

Inserta los valores 1, 2 y 3 usando el método adecuado para una pila.

Imprime el contenido de la pila.

Extrae un elemento de la pila sin usar pop(), guárdalo en una variable e imprímelo.

Extrae otro elemento usando pop() e imprímelo.

Imprime el contenido restante de la pila.

Parte 2: Cola (FIFO - First In, First Out)
Crea una cola vacía.

Inserta los valores 1, 2 y 3 usando el método adecuado para una cola.

Imprime el contenido de la cola.

Extrae un elemento de la cola sin usar pop(), guárdalo en una variable e imprímelo.

Extrae otro elemento usando pop(0) e imprímelo.

Imprime el contenido restante de la cola.
"""

pile1=[]

pile1.append(1)
print(pile1)

pile1.append(2)
print(pile1)

pile1.append(3)
print(pile1)

var1 = pile1[1]
print(var1)


print(pile1[1:])
print(pile1[:2])

#Ejercicio Extra
#Navegación web

stack = []
pos = 0
while True:
    iniciador = input("\nIngresa la URL o navega a traves de *adelante*, *atras*, *salir*: ")
    if iniciador == "adelante":
        pos += 1
        print("Adelantamos una posicion")
        
    elif iniciador == "atras":
        pos -= 1
        print("Retrasamos una posicion")
    elif iniciador == "salir":
        break
    else:
        stack.append(iniciador)
        print(f"Web {iniciador} agregada en la posicion {len(stack)}")
    
    if pos <= 0:
        pos = 0
    elif pos >= len(stack):
        pos = len(stack) -1
    
    print(f"La posición {pos+1} contiene la web {stack[pos]}")


#Impresión en cola

stack = []
pos = 0
while True:
    iniciador = input("\nAgrega el nombre del documeneto a imprimir o *imprimir* o *salir*: ")
    if iniciador == "imprimir":
        if len(stack) == 0:
            print("No hay trabajo en cola para imprimir")
        print(f"Imprimiendo Trabajo: {stack[0]}")
        stack.pop(0)
    
    elif iniciador == "salir":
        break
    
    else:
        stack.append(iniciador)

    print(f"Hay {len(stack)} trabajos en cola para ser impresos")
        
    
