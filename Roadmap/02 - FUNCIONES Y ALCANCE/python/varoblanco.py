
#Funcion Simple
def greet():
    print("Hola, Python!")

greet()


#Función con retorno
def greet_with_return():
    return "Hello python"

print(greet_with_return())


#Función con 1 argumento
def temp (air_temp):
    print(f"Hoy hace {air_temp} grados")

temp(15)

#Función con varios argumentos
def temp_in_time (air_temp, local_time):
    print(f"Hoy hace {air_temp} grados a las {local_time} en punto")

temp_in_time(15, 12)
#Se puede reordenar la declaracion de argumentos y no ponerlos en orden
temp_in_time(local_time=13, air_temp=25)

#Funcion con argumentos predeterminados
def nombre(name="User"):
    print(f"Nombre de usuario {name} logeado")

nombre()
nombre("varoblanco")

#Función con argumentos y return

def usuarios (user1, user2):
    return print(f"Los usuarios {user1} y {user2} estan ahora conectados a tu red")

print(usuarios("Paloma", "Juan"))

#Función con retorno de varios valores y asignarlos a sus variables
def return_varios():
    return "josema", "juan"

greet, names = return_varios()
print(names)
print(greet)

#Función con un número variables de argumentos de entrada
def saludar_a_todos (*names):
    for name in names:
        print(f"Buenos días {name}")

saludar_a_todos("juan", "alfonso", "pelayo", "carmen")

#Funcion con un numero variable de argumentos y palabras clave
def saludar_con_clave_a_todos (**names):
    for key, value in names.items():
        print(f"Parentesco {key} de {value}")

saludar_con_clave_a_todos(padre="juan", hermano="alfonso", primo="pelayo", hija="carmen")

"""
Funciones dentro de funciones
"""

def funcion_exterior():
    print("Salida Ext")
    def funcion_interior():
        print("salida Interior")
    funcion_interior() #Si se llama la ext se ejecuta esta una vez que ha entrado en la funcion

funcion_exterior()
# funcion_interior() da error porque no la ve

"""Funciones del lenguaje"""

print(len("mouredev"))
print(len({1, 2, 3, 4, 5, "hi"}))

print(type(6))
print(type(True))
print(type("Haha"))

print("mouredev".upper())
print("James oNeil".lower())

"""Variables locales y globales"""

var_global=45

print(var_global)

def imprimir():
    print(var_global)

imprimir()

def imprimir_2():
    var_local = 55
    print(var_local)

imprimir_2()
#print(var_local) da error no deja porque no existe fuera de ambito de la funcion imprimir_2

#Extra

def print_nums(cadena1, cadena2):
    count = 0
    for i in range (1, 101):
        if i%3 == 0 and i%5 != 0:
            print(cadena1)
        elif i%5 == 0 and i%3 != 0:
            print(cadena2)
        elif i%5 == 0 and i%3 == 0:
            print(cadena1+cadena2)
        else:
            print(i)
            count+=1
    return count

print(f"Se han impreso {print_nums("Juana", " La loca")} numeros")

