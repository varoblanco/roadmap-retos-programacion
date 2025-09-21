"""Ejercicio"""

import time
import random

import threading


# def greetings():
#     print(f"Buenos dias!")

# def new_user(id: int):
#     greetings()
#     print(f"Nuevo usuario creado con id: {id}")

# new_user(12)

"""EXTRA"""

def tiempo_espera(inicio: int, fin: int):
    return random.randint(inicio, fin)

def conf_cocina_OrdenPlato(name: str):

    time.sleep(tiempo_espera(0,2))
    print(f"Plato: {name}; Confirmación cocina: Orden Recibida")

def conf_cocina_PlatoListo(name: str):

    time.sleep(tiempo_espera(0,7))
    print(f"Plato: {name}; Confirmación cocina: Plato Terminado")

def conf_servicio_PlatoEntregado(name: str):

    time.sleep(tiempo_espera(0,3))
    print(f"Plato: {name}; Confirmación cocina: Plato Servido")


def new_order(name: str):
    print(f"Pedido del plato {name} creado")
    
    print(f"\nEsperando confirmacion cocina (Orden recibida)...")
    conf_cocina_OrdenPlato(name)

    print(f"\nEsperando confirmacion cocina (Plato finalizado)...")
    conf_cocina_PlatoListo(name)

    print(f"\nEsperando confirmacio servicio...(Plato servido)")
    conf_servicio_PlatoEntregado(name)

def new_order_v2(name: str, conf_cocina_OrdenPlato, conf_cocina_PlatoListo, conf_servicio_PlatoEntregado ):
    def process():
        print(f"Pedido del plato {name} creado")
        
        conf_cocina_OrdenPlato(name)
        
        conf_cocina_PlatoListo(name)

        conf_servicio_PlatoEntregado(name)
    threading.Thread(target=process).start()

#new_order("Callos")
new_order_v2("Judias", conf_cocina_OrdenPlato, conf_cocina_PlatoListo, conf_servicio_PlatoEntregado )
new_order_v2("Chuleta", conf_cocina_OrdenPlato, conf_cocina_PlatoListo, conf_servicio_PlatoEntregado )
new_order_v2("Sopa", conf_cocina_OrdenPlato, conf_cocina_PlatoListo, conf_servicio_PlatoEntregado )
new_order_v2("Calamares", conf_cocina_OrdenPlato, conf_cocina_PlatoListo, conf_servicio_PlatoEntregado )