"""
Valor y referencia
"""

# Tipos de dato por valor, los datos se copian en nueva posicion de memoria
var1 = 3
var2 = var1
var2 = 5
print(var1)
print(var2)

# Tipos de dato por referencia, los datos no se copian si no que hacen referencia a la mis direccion de la memoria
list1 = [10, 20]
list2 = list1
list2.append(30)
print(list1)
print(list2)


# Funciones con datos por valor
var3 = 10

def sumar(var: int):
    var = 15
    print(var)

sumar(var3)
print(var3)

# Funciones con datos por referencia SI da problema
list3 = [10, 20]

def sumar_lista(lista: list):
    lista.append(30)
    print(lista)

sumar_lista(list3)
print(list3)

"""EXTRA"""

def intercambio_por_valor(palabra1: str, palabra2: str):
    temp = palabra1
    palabra1 = palabra2
    palabra2 = temp
    return palabra1, palabra2

print(intercambio_por_valor("salsa", "hoja"))

def intercambio_por_referncia(palabra1: list, palabra2: list):
    temp = palabra1
    palabra1 = palabra2
    palabra2 = temp
    return palabra1, palabra2

print(intercambio_por_referncia(["soja", "dulce"], ["Chile", "picante"]))