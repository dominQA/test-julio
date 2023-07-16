import json
from datetime import datetime

from src.POM.Pages.api_exercise.po_pet import Pet
from src.POM.Pages.api_exercise.po_pet_store import PetStore
from test.helpers.utils import Utils

"""
1.	Crear usuario mediante petición HTTP y posteriormente recuperar sus datos llamando al servicio correspondiente. 

2.	Recoger mediante petición HTTP, el JSON que retorna el endpoint “/pet/findByStatus” y listar mediante una función los nombres de las mascotas que se hayan vendido. 
   a. El formato de salida debe de estar formado por la tupla {id, name}. 
   b. Se puede utilizar la estructura de datos que se prefiera. 

3.	Crear una clase cuyo constructor requiera de la estructura de datos anterior y realizar un método que pueda recorrerla para poder identificar cuantas mascotas se llaman igual.
a. Ejemplo de salida: {“William”:11, “Floyd”:2}.
Como output se pide el código y los resultados de salida de los puntos anteriores. 
"""


def get_list_pets_by_status(status):
    """
    Get a list of the pets with the status passed by parameter.
    :param status:
    :return response:
    """
    po_api = PetStore()
    response = po_api.get_pets_by_status(status)
    print('* Status code [Get pets by status]: ', response.status_code)

    date = str(datetime.now().strftime("\n\n%d-%m-%Y - %H:%M:%S\n"))
    output = "* Status code [Get pets by status]: '" + str(response.status_code)
    if response.status_code == 200:
        response_body = json.loads(response.text)
        sold_pets = po_api.obtain_pets_list(response_body)
        print(">>> PETS SOLD:\n", sold_pets)
        output += "\n>>> PETS SOLD:\n" + str(sold_pets)
        Utils.save_report(date + "API EXECUTION: \n" + output)
        return sold_pets


if __name__ == '__main__':
    pet_status = "sold"
    pets_data = get_list_pets_by_status(pet_status)

    po_pet = Pet(pets_data)
    pet_count = po_pet.count_same_name_pets()
