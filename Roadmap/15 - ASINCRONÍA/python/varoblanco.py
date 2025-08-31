"""Ejercicio"""
from datetime import datetime, timedelta
import time
import asyncio

async def delay(name: str, delay_secs: int):
    
    time_start = datetime.now()
    time_finish = time_start + timedelta(seconds=delay_secs)

    print(f"\nLa funcion {name} se ejecutará durante {delay_secs} segundos.")
    print(f"Funcion {name}, hora de inicio: {time_start.strftime("%H:%M:%S")} ")

    while datetime.now() < time_finish:
        # print(".")
        # print("..")
        await asyncio.sleep(0.5)
    
    print(f"Funcion {name}, {delay_secs} segundos, confirmacion inicio: {time_start.strftime("%H:%M:%S")}, fin: {datetime.now().strftime("%H:%M:%S")}")
    
# asyncio.run(delay("P1", 1))

"""EXTRA"""

# asyncio.run(delay("C", 3))
# asyncio.run(delay("B", 2))
# asyncio.run(delay("A", 1))
# asyncio.run(delay("D", 1))

async def wait_functions():
    await asyncio.gather(delay("C", 3), delay("B", 2), delay("A", 1))
    await delay("D", 1)

asyncio.run(wait_functions())


