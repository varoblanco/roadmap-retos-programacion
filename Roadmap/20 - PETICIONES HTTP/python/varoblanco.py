import requests

"""Ejercicio"""


# response = requests.get("https://moure.dev")

# print(response)
# if response.status_code == 200:
#     print(response.text)
# else:
#     print(f"erorr de codigo {response.status_code} al relaizar la peticón")

"""EXTRA"""

pkmn = input("Seleccione Pokemon: ")


response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pkmn}")

if response.status_code == 200:

    response_evo_url = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pkmn}")
    
    if response_evo_url.status_code == 200:
        
        response_evo = requests.get(response_evo_url.json()["evolution_chain"]["url"])
        
        if response_evo.status_code == 200:

            opcion = "1"

            while opcion != "4":
                opcion = input("Seleccion tipo que información que quiere obtener:\n[1] Información del pokemon" \
                "\n[2] Línea Evolutiva \n[3] Juegos en los que aparece \n[4] Salir \n-->: ")

                match opcion:
                    case "1":
                        print(response.json()["name"])

                        print(response.json()["id"])

                        print(response.json()["weight"])

                        print(response.json()["height"])
                        
                        for types in response.json()["types"]:
                                print(types["type"]["name"])

                    case "2":
                        ev0 = response_evo.json()["chain"]["species"]["name"]

                        ev1 = response_evo.json()["chain"]["evolves_to"][0]["species"]["name"]

                        ev2 =response_evo.json()["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]

                        print(f"{ev0.upper()} --> {ev1.upper()} --> {ev2.upper()}  ")

                    case "3":
                        games_avaliable = []

                        for games in response.json()["game_indices"]:
                            games_avaliable.append(games["version"]["name"])

                        print(games_avaliable)
        else:
            print(f"Error obteniendo evo, error = {response.status_code}")
    else:
        print(f"Error obteniendo link evo, error = {response.status_code}")
else:
    print(f"Error obteniendo info pokemon, error = {response.status_code}")