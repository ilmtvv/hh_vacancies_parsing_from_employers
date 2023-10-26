import requests

from src.employers_id import list_of_employers_id


def get_vacancies(url_employer: str) -> list:
    """
    Получение вакансий.
    """

    list_of_vacancies = []

    for employer in list_of_employers_id:

        response = requests.get(url_employer + employer)
        data_employer = response.json()

        response = requests.get(data_employer['vacancies_url'])
        data_vacancies = response.json()
        list_of_vacancies.extend(data_vacancies['items'])

    return list_of_vacancies


def get_name_company(url_employer: str) -> dict:
    """
    Получение словаря с именами компаний.

    """
    dict_of_name_company = {}

    for employer in list_of_employers_id:

        response = requests.get(url_employer + employer)
        data_employer = response.json()

        dict_of_name_company[employer] = data_employer['name']

    return dict_of_name_company
