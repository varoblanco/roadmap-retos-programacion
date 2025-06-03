#Ejercicio Herencia y Polimorfismo

class Animal:
    def __init__(self, name: str):
        self.name = name
        
    def sound(self):
        pass

class Dog(Animal):

    def sound(Animal):
        print("Guau!")

class Cat(Animal):

    def sound(self):
        print('Miau')

def print_sound(animal: Animal):
    animal.sound()


my_animal = Animal("Pepe")
my_animal.sound()

my_dog = Dog("Oli")
my_dog.sound()

my_cat = Cat("Pepper")
my_cat.sound()

my_dog.sound()


#Ejercicio Extra

class Empleado:

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id


class Gerente(Empleado):
    pass

class Gerente_Proyectos(Empleado):
    pass

class Programador(Empleado):
    def __init__(self, name, id):
        super().__init__(name, id)
    pass

empleado1 = Empleado ("Juan", 5)