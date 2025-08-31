from datetime import datetime

"""Ejercicio"""

time_now = datetime.now()
time_birth = datetime.strptime("23-10-1991 18:00:25", "%d-%m-%Y %H:%M:%S")
print(datetime.date(time_now))
print(type(time_now))

print(time_birth)
print(type(time_birth))

print(f"Han transccurrido {time_now.year-time_birth.year} desde hoy a cuiando nací")
print(type(time_now.year-time_birth.year))

"""EXTRA"""

#  * - Día, mes y año.
print(f"Día mes y año de mi nacimiento: {time_birth.strftime("%d/%m/%y")}")

#  * - Hora, minuto y segundo.
print(f"Hora minuto y segundo de mi nacimiento: {time_birth.strftime("%H:%M:%S")}")

#  * - Día de año.
print(f"Nº de dia en el año de mi nacimiento: {time_birth.strftime("%j")}")

#  * - Día de la semana.
print(f"Día de la semana de mi nacimiento: {time_birth.strftime("%a - %A")}")

#  * - Nombre del mes.
print(f"Mes de mi nacimiento: {time_birth.strftime("%b - %B")}")

