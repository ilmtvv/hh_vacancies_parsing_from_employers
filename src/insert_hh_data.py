from src.hh_parser import get_vacancies, get_name_company

from src.config_db import params

import psycopg2

url_employers = "https://api.hh.ru/employers/"


def insert_employers_data():

    con = psycopg2.connect(dbname="hh_vacancies", **params)
    con.autocommit = True
    cur = con.cursor()

    name_company = get_name_company(url_employers)
    for key in name_company:
        cur.execute("INSERT INTO employers VALUES (%s, %s) ON CONFLICT (id_employer) DO NOTHING", (int(key), name_company[key]))

    cur.close()
    con.close()


def insert_vacancies_data():

    con = psycopg2.connect(dbname="hh_vacancies", **params)
    con.autocommit = True
    cur = con.cursor()

    vacancies = get_vacancies(url_employers)
    for vacancy in vacancies:

        id_vacancy = vacancy['id']
        id_employer = vacancy['employer']['id']
        name_vacancy = vacancy['name']
        url_vacancy = vacancy['alternate_url']

        if vacancy['salary'] is None:
            salary = None
        elif vacancy['salary']['from'] is None:
            salary = vacancy['salary']['to']
        elif vacancy['salary']['to'] is None:
            salary = vacancy['salary']['from']
        else:
            salary = int((vacancy['salary']['to'] + vacancy['salary']['from']) / 2)

        cur.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id_vacancy) DO NOTHING", (id_vacancy, id_employer, name_vacancy, url_vacancy, salary))

    cur.close()
    con.close()
