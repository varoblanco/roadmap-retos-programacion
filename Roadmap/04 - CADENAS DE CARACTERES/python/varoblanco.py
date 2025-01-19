s1 = "Hola"
s2 = "mundo"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1*2 + " " + s2)

# Indexación
print(s1[0] + s1[1])

# Longitud
print(len(s1))

# Slicing (porción)
print(s1[:2])
print(s1[2:])

# Busqueda
print("a" in s1)
print("a" in s2)

# Reemplazo
print(s1.replace("a", "o")) # no lo cambia permanentemente
print(s1)

# División
print(s2.split("d"))

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())

print("Alvaro Blanco".title())
print("Alvaro Blanco".capitalize())

# Eliminación de espacios al principio y al final
print(" Hola a todos  ")
print(" Hola a todos  ".strip())

# Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("la"))
print(s1.endswith("la"))
print(s1.endswith("do"))

# Búsqueda de posición
s3 = "Alvaro Blanco varoblanco@gmail.com"

print(s3.find("varo"))
print(s3.find("blanco")) #Encuentra el segundo pero no el primero porque hay mayus
print(s3.lower().find("blanco")) #Se baja todo a minus y si encuentra uno

# Búsqueda de ocurrencias
print(s3.lower().count("v"))

# Formateo
print("FORMATEO: Primera palabra: {}, segunda palabra: {}".format(s1, s2))

# Interpolación
print(f"INTERPOLACION: Primera palabra: {s1}, segunda palabra: {s2}")

# Tranformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!" ]
print("".join(l1))
print(type("".join(l1)))

# Transformaciones numéricas
s4 = "1234"
print(s4)
print(type(s4))
s4 = int(s4)
print(s4)
print(type(s4))

s4 = "1234.4455"
print(s4)
print(type(s4))
s4 = float(s4)
print(s4)
print(type(s4))

#s4 = "1,445" SIEMPRE MAL, PONER SIEMPRE PUNTO .


# Comprobaciones varias
print("\n")
s1 = "Hola"
print(s1)
print(s1.isalnum())
print(s1.isalpha())
print(s1.isnumeric())

print("\n")
s2 = "Hola1234"
print(s2)
print(s2.isalnum())
print(s2.isalpha())
print(s2.isnumeric())

print("\n")
s3="1234"
print(s3)
print(s3.isalnum())
print(s3.isalpha())
print(s3.isnumeric())

#s4 = 12 NO tiene sentido porque solo vale para str

print("\n")
s5 = "??"
print(s5)
print(s5.isalnum())
print(s5.isalpha())
print(s5.isnumeric())

"""EXTRA"""

#Check palindromo

palabra1 = input("Introduzca palabra nº1: ").lower()
palabra2 = input("Introduzca palabra nº2: ").lower()

"""Version varoblanco
def checkpalindromo (word1, word2):
    if len(palabra1) != len(palabra2):
        return False
    else:
        check = 0
        longitud = len(word1)
        for i in range(longitud):
            if word1[i] == word2[(longitud-1)-i]:
                check += 1
        if check == longitud:
            return True
        else:
            return False
        
if checkpalindromo(palabra1, palabra2):
    print("SÍ son palindromos")
else:
    print("NO son palindromos")
"""
print(f"¿ Es {palabra1} un palindromo? {palabra1 == palabra1[::-1]}")
print(f"¿ Es {palabra2} un palindromo? {palabra2 == palabra2[::-1]}")

print(palabra1)
print(palabra1[::-1])

print(f"¿ Es {palabra1} un anagrama de {palabra2}? {sorted(palabra1) == sorted(palabra2)}")

