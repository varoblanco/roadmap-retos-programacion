#Ejercicio Basico

class Programador:

    surname = "Blanco"

    def __init__(self, name: str, age: int, lenguajes: list):
        self.name = name
        self.age = age
        self.lenguajes = lenguajes
        pass
    
    def print(self):
        print(f"Programador {self.name} | Apellido: {self.surname} | Edad: {self.age} | Lenguajes: {self.lenguajes}")

my_programmer = Programador("Alvaro", 33, ["python", "JS"])
my_programmer.print()
my_programmer.surname = "Vallina"
my_programmer.print()
my_programmer.age = 32
my_programmer.print()

#Usar clases para pila y cola

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def count(self):
        print(f"La pila tiene {len(self.stack)} posiciones")

    def print(self):
        print(f"La pila contiene: {self.stack}")

my_stack = Stack()
my_stack.push("Arroz")
my_stack.push("Carne")
my_stack.push("Pescado")
my_stack.print()
my_stack.pop()
my_stack.print()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        self.queue.pop(0)

    def count(self):
        print(f"La Lista tiene {len(self.queue)} posiciones")

    def print(self):
        print(f"La Listaila contiene: {self.queue}")

mylist = Queue()
mylist.enqueue("Madera")
mylist.enqueue("Cabrón")
mylist.enqueue("Agua")
mylist.print()
mylist.dequeue()
mylist.print()