
"""Ejercicio"""

import re

text = "Mi numero es 656 835 645 y mi correo es algo123@gmail.com siendo mi web https://espacioblanco.es"

try :
    print(f"Primera palabra: {re.search(r"^\w+", text).group()}")

    print(f"Buscar movil: {re.search(r"\W6\d{2}\W?\d\W?\d\W?\d\W?\d\W?\d\W?\d\s", text).group()}")

    print(f"Buscar email: {re.search(r"\W\w*[@]\w*[.]\w*", text).group()}")

    print(f"Nª 3 cifras con search: {re.search(r"\d{3}", text).group()}")

    print(f"Nª 3 cifras con findall: {re.findall(r"\d{3}", text)}")

    print(f"Dejar solo los ultimos 3 numeros privacidad: {re.sub(r"\d", "X", text)}")

    print(f"Buscar url: {re.search(r'https?://?\w*[.]\w{2,3}', text).group()}")

except AttributeError:
    print(f"No se encontró regex solicitado en el texto")

