from config_db import params

import psycopg2

con = psycopg2.connect(dbname='postgres', **params)

con.autocommit = True

cur = con.cursor()

cur.execute(f"CREATE DATABASE hh_vacancies")

cur.close()

con.close()
