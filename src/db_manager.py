from src.config_db import params

from src.hh_parser import get_name_company

import psycopg2

url_employers = "https://api.hh.ru/employers/"


class DBManager:
    con = psycopg2.connect(dbname="hh_vacancies", **params)
    con.autocommit = True
    cur = con.cursor()

    def get_companies_and_vacancies_count(self):

        employers = get_name_company(url_employers)

        dict_count_vacancies = {}

        for key in employers:
            self.cur.execute(f"SELECT COUNT(*) FROM vacancies WHERE id_employer = {int(key)} GROUP BY id_employer")
            count = self.cur.fetchone()
            dict_count_vacancies[employers[key]] = count[0]

        for key in dict_count_vacancies:
            print(key, ' ', dict_count_vacancies[key])

    def get_all_vacancies(self):

        dict_name_company = get_name_company(url_employers)

        self.cur.execute(f"SELECT * FROM vacancies")
        vacancies = self.cur.fetchall()

        for vacancy in vacancies:
            vacancy = list(vacancy)
            vacancy[1] = dict_name_company[str(vacancy[1])]
            print(*vacancy)

    def get_avg_salary(self):

        self.cur.execute(f"SELECT AVG(salary) FROM vacancies")
        avg_salary = self.cur.fetchone()

        return int(avg_salary[0])

    def get_vacancies_with_higher_salary(self):

        avg_salary = self.get_avg_salary()
        self.cur.execute(f"SELECT * FROM vacancies WHERE salary > {avg_salary}")
        highter_salary = self.cur.fetchall()

        print(*highter_salary, sep='\n')

    def get_vacancies_with_keyword(self, keyword):

        self.cur.execute(f"SELECT name_vacancy, url_vacancy, salary FROM vacancies")
        vacancies_with_keyword = self.cur.fetchall()

        for vacancy in vacancies_with_keyword:
            name = vacancy[0].lower()

            if keyword.lower() in name:
                print(*vacancy)
