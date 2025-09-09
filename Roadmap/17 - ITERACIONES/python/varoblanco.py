"""Ejercicio"""

print("\nCon for")
for i in range (0,10):
    print(i+1)

print("\nCon while")
i = 0
while i <10:
    print(i+1)
    i+=1

print("\nCon recursividad e if")
i = 0
def imprimir(i):
    if i<10:
        print(i+1)
        imprimir(i+1)
imprimir(i)

"""EXTRA"""

print("\nRecorriento Listas (mutables)")
for e in [1, 2, 3, 4, 5]:
    print(e)

print("\nRecorriento Tuplas (inmutables)")
for e in (1, 2, 3, 4, 5):
    print(e)

print("\nRecorriento Diccionarios")
for e in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}.keys():
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}.values():
    print(e)

print("\nCon comprehensions lists")
print(*[i+1 for i in range (0, 10)], sep="\n")

for c in "Python":
    print(c)

for c in reversed([1, 2, 3, 4]):
    print(c)

for c in sorted(["b", "l", "a", "n", "c", "o"]):
    print(c)

for i, c in enumerate(["b", "l", "a", "n", "c", "o"]):
    print(f"Índice: {i}, valor: {c}")
