"""
MANEJO DE EXCEPCIONES
"""

try:
    print(10/0)
    my_list = [1, 2, 3]
    print(my_list[6])

except Exception as e:
    print(f"Se ha producido el error: {e} ({type(e).__name__})")


"""Extra"""

def StrTypeError(Exception):
    pass


def process_params(parameters: list):
    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("Tercer elemento como str, incorrecto")
    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1,2,"abv", 4])
except IndexError as e:
    print(f"Se ha producido un error al haber menos de 3 posiciones")
except ZeroDivisionError as e:
    print(f"Se ha producido un error al haber un 0 en la segunda posicion")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado de tipo: {e}")
else:
    print("No se han producido errores")
finally:
    print("Se finaiza el programa")