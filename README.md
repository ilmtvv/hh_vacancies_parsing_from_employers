парсанг вакансий по id работодателей и заполнение ими дб

id работодателей находятся в src/employers_id.py в списке

1 - необходимо создать файл параметров подключение к дб config_db.py в src

params = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '',
    'port': '5432',
}

2 - запустить src/create_db.py

3 - запустить main.py
