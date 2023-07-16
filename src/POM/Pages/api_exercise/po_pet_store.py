import requests
import re


class PetStore:
    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2'
        self.header = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

    def create_user(self, username, email):
        """
        Create a new user with the information passed by parameter.
        :param username:
        :param email:
        :return:
        """
        url = f'{self.base_url}/user'
        data = {
            "id": 1,
            "username": username,
            "firstName": "MR",
            "lastName": "SD",
            "email": email,
            "password": "1234",
            "phone": "666666666",
            "userStatus": 1
        }

        response = requests.post(url,
                                 headers=self.header,
                                 json=data)
        response.raise_for_status()
        return response

    def get_user(self, username):
        """
        Get the user data through the username passed by parameter.
        :param username:
        :return:
        """
        url = f"{self.base_url}" + "/user/" + username
        response = requests.get(url, headers=self.header)
        response.raise_for_status()
        return response

    def get_pets_by_status(self, status):
        """
        Get a list of the pets by status, which is passed by parameter.
        Available values: 'available', 'pending', 'sold'.
        :param status:
        :return:
        """
        url = f'{self.base_url}' + "/pet/findByStatus?status=" + status
        response = requests.get(url, headers=self.header)
        response.raise_for_status()
        return response

    @staticmethod
    def obtain_pets_list(response_body):
        """
        Obtain a list of the pets that have id and name. Due to this is an API website, where people use to try and
        test different alternatives, special characters have been avoided.
        :param response_body:
        :return:
        """
        sold_pets = []
        for pet in response_body:
            if ('name' in pet) and ('id' in pet):
                id_pet = pet['id']
                name_pet = pet['name']
                new_name_pet = re.sub(r"[^a-zA-Z]", '', name_pet)
                sold_pets.append((id_pet, new_name_pet))
        return sold_pets
