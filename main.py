from src.insert_hh_data import insert_employers_data, insert_vacancies_data

from src.db_manager import DBManager

def main():

    insert_employers_data()
    insert_vacancies_data()

    manager = DBManager()

    manager.get_companies_and_vacancies_count()


if __name__ == '__main__':
    main()