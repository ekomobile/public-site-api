from config.settings import CACHE_DIR
import requests
from typing import Optional
import os


class DealersAPI:
    def __init__(self):
        self.__auth_url: str = os.getenv("DEALERS_API_AUTH_URL")
        self.__auth_login: str = os.getenv("DEALERS_API_AUTH_LOGIN")
        self.__auth_password: str = os.getenv("DEALERS_API_AUTH_PASSWORD")
        self.__get_numbers_list_url: str = os.getenv("DEALERS_API_GET_NUMBERS_LIST_URL")
        self.__token: Optional[str] = None

    @staticmethod
    def __set_current_token(new_token):
        with open(CACHE_DIR.joinpath('dealers_api_token.txt'), 'w') as cached_token:
            cached_token.write(new_token)

    @staticmethod
    def __get_current_token():
        try:
            with open(CACHE_DIR.joinpath('dealers_api_token.txt'), 'r') as cached_token:
                return cached_token.read()
        except FileNotFoundError:
            return None

    def __get_new_token(self) -> None:
        auth_request: requests = requests.get(
            self.__auth_url, params={
                'login': self.__auth_login,
                'password': self.__auth_password
            }
        )

        with auth_request as auth_response:
            if auth_response.json()['data'] is None:
                new_token = 'undefined'
            else:
                new_token = str(auth_response.json()['data']['token'])
            self.__set_current_token(new_token)

    def __check_token(self):
        current_token = self.__get_current_token()
        if current_token is None or current_token.__len__() == 0:
            self.__get_new_token()
            self.__token = self.__get_current_token()
        else:
            self.__token = current_token

    def __get_request(self):
        return requests.get(self.__get_numbers_list_url, params={'token': self.__token})

    def __send_request(self):
        numbers_list_request = self.__get_request()

        with numbers_list_request as numbers_list_response:
            return numbers_list_response

    def get_phone_numbers_list(self):
        self.__check_token()
        response = self.__send_request()
        if int(response.json()['status']) == 401:
            self.__get_new_token()
            self.__check_token()
            response = self.__send_request()

        return response.json()['data']['phoneList']
