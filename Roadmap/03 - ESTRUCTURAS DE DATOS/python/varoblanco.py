"""
Estructuras
"""

"""Listas, son lo mismo que las tuplas pero se pueden cambiar, mas lentas de acceso, pensado para datos dinámicos, más métodos"""

var1=[1, 2, 3]
var1: list=[1, 2, 3] #Clarificacion de lista, forma mas correcta
print(var1)

#Insercción
var1.append("Some")
print(var1)

#Eliminación
var1.remove(2)
print(var1)

#Acceso a una posición
print(var1[0])
print(var1[1])
print(var1[2])

#Actualización de una posición
var1[2]="Algo"
print(var1)

#Ordenación
var2: list=[56, 76, 32, 54, 89, 32]
var2.sort()
print(var2)
print(type(var2))


"""Tuplas, son lo mismo que las listas pero no pueden cambiar, mas rapidas de acceso, pensado para datos estáticos, menos métodos"""
var3: tuple=(1, 2, 3)
print(var3)
#var3[2]=12 Da Error no se puede cambiar

#Acceso
print(var3[1])

#Ordenación
var4: tuple=(43, 38, 609, 62, 57, 69)
var4 = tuple(sorted(var4)) #Ojo mirar como se ordenan las tuplas
print(var4)
print(type(var4))

"""Sets, no puede haber duplicados, no se guardan con orden, buenos para check id"""

# Detectar duplicados en una lista de nombres
names1 = ["Alice", "Bob", "Alice", "Charlie", "Bob"] #Versión con lista donde puede haber duplicados
print(names1)  # Salida: {'Alice', 'Charlie', 'Bob'}

names = {"Alice", "Bob", "Alice", "Charlie", "Bob"}
print(names)  # Salida: {'Alice', 'Charlie', 'Bob'}

unique_names = set(names) #Froma rapida de sacar duplicados
print(unique_names)  # Salida: {'Alice', 'Charlie', 'Bob'}
print(type(unique_names))  # Salida: {'Alice', 'Charlie', 'Bob'}

#Adicción
names.add("Laura")
print(names)

#Eliminación
names.remove("Bob")
print(names)

names = set(sorted(names))#No se puede ordenar
print(names)

#Diccionario
my_dict: dict = {
    "name": "Alvaro" ,
    "email": "varoblanco@gmail.com",
    "edad": 33
}

#Insercción
my_dict["lugar nacimiento"] = "Oviedo"
print(my_dict)

#Eliminacion
del my_dict["email"]
print(my_dict)

#Accesso
print(my_dict["name"])

#Actualizacion
my_dict["edad"] = 36
print(my_dict)

#Ordenacion
my_dict = dict(sorted(my_dict.items()))
print(my_dict)

"""EXTRA"""

def agenda_contactos():
    agenda: list = [] 
    valor_input = 0
    while valor_input!= 4:
        valor_input = int(input("""\n\nBIENVENIDO A LA AGENDA\n
Siga las indicaciones\n
[1] Para Búsqueda de un contacto en la agenda \n
[2] Para Añadir un contacto a la agente \n
[3] Para Actualizar un contacto en la agenda \n
[4] Para Salir de la Agenda\n
-->"""))
        match valor_input:
            case 1:
                nombre = input("Introduzca el nombre del contacto a buscar --> ")
                count = 0
                for items in agenda:
                    if items["nombre"]==nombre:
                        print(f"\nNombre: {items["nombre"]}\nTelefono: {items["telefono"]}")
                        count +=1
                if count == 0:
                        print("No se encuentra contacto")
            case 2:
                nombre = input("Introduzca el nombre del contacto a añadir --> ")
                tel = int(input("Introduzca el número de teléfono del contacto a añadir --> "))
                agenda.append({"nombre": nombre, "telefono": tel})
            case 3:
                nombre = input("Introduzca el nombre del contacto para actualizar el telefono")
                count = 0
                for items in agenda:
                    if items["nombre"]==nombre:
                        items["telefono"] = int(input("Introduzca el número de teléfono --> "))
                        print(f"Nombre: {items["nombre"]}\nTelefono: {items["telefono"]}")
                if count == 0:
                        print("No se encuentra contacto")
        
agenda_contactos()     
