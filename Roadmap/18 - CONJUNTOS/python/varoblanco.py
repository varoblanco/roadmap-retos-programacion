"""Ejercicio"""
#Necesitamos una estructura tipo lista [] mutables y ordenadas

data = [1, 2, 3, 4]
print(f"Estructura inicial: {data}")

data.append("a")
print(f"Con append al final: {data}")

data.insert(0, "b")
print(f"Insertando en inicio: {data}")

data.extend([9, 8, 7])
print(f"Haciendo extend para un grupo al final {data}")

#Ejemplo de que se inserta una lista dentro de una lista
#data.insert(2, [9, 8, 7])
#print(f"Inserción erronea de lista en lista: {data}")

#Para hacer esto bien hay que hacer un slice
data[3:3] = [9, 8, 7]
print(f"Hacinedo slice en posicion especifica: {data}")

del data[1]
print(f"Eliminando valor en posicion 1: {data}")

data[0] = "c"
print(f"Modificar valor especifico pos 0: {data}")

if "c" in data:
    print("Si está")
else:
    print("No lo está")

data.clear()
print(data)

"""EXTRA"""

elements_1 = [1, 2, 3, 4]
elements_2 = [1, 2, 3, 4, 5, 6]
elements_3 = [7, 8, 9, 10]

elements_1.extend(elements_2)
print(elements_1)

set_1 = {1, 2, 3, 4}
set_2 = {2, 3, 4, 5, 6}
set_3 = {7, 8, 9, 10}

print(set_1)
print(set_2)

print(f"Union de sets: {set_1.union(set_2)}")
print(f"Interseccion de sets: {set_1.intersection(set_2)}")
print(f"Diferencias de set1 vs 2: {set_1.difference(set_2)}")
print(f"Diferencias de set2 vs 1: {set_2.difference(set_1)}")
print(f"Diferencias total entre 1 y 2, todo lo que no es común: {set_1.symmetric_difference(set_2)}")