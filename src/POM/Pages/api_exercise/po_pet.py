"""
3.	Crea una clase cuyo constructor requiera de la estructura de datos anterior y realiza un método que pueda
recorrerla para poder identificar cuantas mascotas se llaman igual.
    - Ejemplo de salida: {“William”: 11, “Floyd”: 2} Como output, te pediremos el código (puedes separarlo en archivos
    como quieras) y los resultados de salida de los puntos anteriores.
"""
from test.helpers.utils import Utils


class Pet:

    def __init__(self, pet_id_and_name):
        self.pet_id_and_name = pet_id_and_name

    def count_same_name_pets(self):
        """
        Counts how many pets have the same name.
        :return:
        """
        pet_names_data = {}
        for pet in self.pet_id_and_name:
            name_pet = pet[1]
            if name_pet not in pet_names_data:
                pet_names_data[name_pet] = 1
            else:
                pet_names_data[name_pet] += 1
        print('\n>>> Number of pets with the following names:')
        print(pet_names_data)
        output = ">>> Number of pets with the following names:\n" + str(pet_names_data)
        Utils.save_report(output)
