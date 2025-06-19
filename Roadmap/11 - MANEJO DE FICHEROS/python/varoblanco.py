"""Ejercicio"""

import os

my_file = "varoblanco.txt"

with open(my_file, "w") as file:
    file.write("Varoblanco\n")
    file.write("36\n")
    file.write("Python")

with open(my_file, "r") as file:
    print(file.read)

os.remove(my_file)

"""Extra"""

my_file = "varoblanco_shop.txt"

open(my_file, "a")

while True:
    print("\n1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular Venta Total")
    print("7. Calcular Venta por producto")
    print("8. Salir")

    option = input("\nEscoge una opción: \n")

    if option == "1":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(my_file, "a") as file:
            file.write(f"{name}, {quantity}, {price}")
    
    elif option == "2":
        product = input("Producto a consultar: ")
        with open(my_file, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == product:
                    print(line)
     
    elif option == "3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(my_file, "r") as file:
            lines = file.readlines()
        with open(my_file, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                   file.write(f"{name}, {quantity}, {price}\n")
                else:
                     file.write(line)
                
    elif option == "4":
        name = input("Nombre: ")
        with open(my_file, "r") as file:
            lines = file.readlines()
        with open(my_file, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                   pass
                else:
                     file.write(line)
    
    elif option == "5":
        with open(my_file, "r") as file:
            print(f"\n{file.read()}")
    
    elif option == "6":
        suma = 0
        with open(my_file, "r") as file:
            lines = file.readlines()
        for line in lines:
            suma += int(line.split(", ")[1]) * int(line.split(", ")[2])
        print(f"\nLa suma total de todo el almacen es: {suma}")
    
    elif option == "7":
        name = input("Nombre: ")
        suma = 0
        with open(my_file, "r") as file:
            lines = file.readlines()
        for line in lines:
            if line.split(", ")[0] == name:
                suma += int(line.split(", ")[1]) * int(line.split(", ")[2])
            else:
                pass
        print(f"\nLa suma total de {name} en el almacen es de: {suma} €")
            
    elif option == "8":
        os.remove(my_file)
        break



          
