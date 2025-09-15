"""Ejercicio"""

from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(number: int):
    print(Weekday(number))

get_day(1)


"""EXTRA"""

class Order_status (Enum):
    PENDIENTE = 1
    ENVIADO = 2 
    ENTREGADO = 3
    CANCELADO = 4

class Order:

    status = Order_status.PENDIENTE

    def __init__(self, id: int):
        self.id = id
    
    def ship(self):
        if self.status == Order_status.PENDIENTE:
            self.status = Order_status.ENVIADO
        else:
            print(f"El pedido ha de estar pendiente para ser enviado")
        self.show_satus()

    def delivered(self):
        if self.status == Order_status.ENVIADO:
            self.status = Order_status.ENTREGADO
        else:
            print(f"El pedido ha de estar enviado para ser entregado")
        self.show_satus()

    def cancel(self):
        if self.status != Order_status.ENTREGADO:
            self.status = Order_status.CANCELADO
        else:
            print(f"El pedido ha de NO estar entregado para ser cancelado")
        self.show_satus()

    def show_satus(self):
        print(f"El estado del pedido {self.id} es: {self.status.name}")
        
order_1 = Order(1)

order_1.show_satus()
order_1.delivered()

order_1.ship()

order_1.cancel()
