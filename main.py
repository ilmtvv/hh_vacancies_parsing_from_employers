from src.insert_hh_data import insert_employers_data, insert_vacancies_data

from src.db_manager import DBManager

def main():

    insert_employers_data()
    insert_vacancies_data()

    manager = DBManager()

    print("""
1 - получение вакансий и количества вакансий у них
2 - получение всех вакансий
3 - получение avg зарплат
4 - получение вакансий у которой зп больше avg
5 - получение вакансий по слову
стоп - выход
""")

    while True:


        user_input = input()

        if user_input == '1':
            manager.get_companies_and_vacancies_count()
        elif user_input == '2':
            manager.get_all_vacancies()
        elif user_input == '3':
            print(manager.get_avg_salary())
        elif user_input == '4':
            manager.get_vacancies_with_higher_salary()
        elif user_input == '5':
            manager.get_vacancies_with_keyword(input('введите слово\n'))
        elif user_input == 'стоп':
            break

if __name__ == '__main__':
    main()