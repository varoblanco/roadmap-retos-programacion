
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

#Funcion con 