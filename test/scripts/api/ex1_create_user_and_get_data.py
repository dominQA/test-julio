from datetime import datetime
from src.POM.Pages.api_exercise.po_pet_store import PetStore
import json

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


def create_new_user():
    """
    Create new user and check the response status code.
    :return:
    """
    po_api = PetStore()
    create_user_response = po_api.create_user(username_new, email)
    if not create_user_response.status_code == 200:
        print(">>> User NOT created.")
    print(">>> User created successfully.")
    print("* Status code [User creation]: ", create_user_response.status_code)
    assert create_user_response.status_code == 200
    output = ">>> User created successfully.\n" \
             "* Status code [User creation]: " + str(create_user_response.status_code)
    date = str(datetime.now().strftime("\n\n%d-%m-%Y - %H:%M:%S\n"))
    Utils.save_report(date + "API EXECUTION: \n" + output)


def get_user_data(username):
    """
    Get the user data through the username passed by parameter.
    :param username:
    :return response:
    """
    po_api = PetStore()
    response = po_api.get_user(username)
    print('* Status code [Get user data]: ', response.status_code)
    output = "* Status code [Get user data]: " + str(response.status_code)
    if response.status_code == 200:
        response_body = json.loads(response.text)
        print(">>> User data received: \n", response_body)
        output += "\n>>> User data received: \n" + str(response_body)
    assert response.status_code == 200
    Utils.save_report(output)


# User data
username_new = "Pepito"
email = "user@example.com"

if __name__ == '__main__':
    create_new_user()
    get_user_data(username_new)
