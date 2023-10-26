from config_db import params

import psycopg2

con = psycopg2.connect(dbname='postgres', **params)

con.autocommit = True

cur = con.cursor()

cur.execute(f"DROP DATABASE hh_vacancies")

cur.execute(f"CREATE DATABASE hh_vacancies")

cur.close()

con.close()

con = psycopg2.connect(dbname='hh_vacancies', **params)

con.autocommit = True

cur = con.cursor()

cur.execute("""
    CREATE TABLE employers (
        id_employer INT PRIMARY KEY,
        name_employer VARCHAR(100)
    )
""")

cur.execute("""
    CREATE TABLE vacancies (
        id_vacancy INT PRIMARY KEY,
        id_employer INT,
        name_vacancy VARCHAR(100),
        url_vacancy VARCHAR(200),
        salary INT
    );
    ALTER TABLE vacancies ADD CONSTRAINT fk_vacancies_employer FOREIGN KEY(id_employer) REFERENCES employers(id_employer)
""")

cur.close()

con.close()
