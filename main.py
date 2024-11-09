import psycopg2
from src.hh_api import get_employees, load_vacancies

from src.DBManager import DBManager
from src.config import config
from src.db import DB


def main():
    params = config()

    data_emp = get_employees()
    data_vac = load_vacancies(data_emp)
    db = DB(params)
    db.save_data_employer(data_emp)
    db.save_data_vacancies(data_vac)
    db_manager = DBManager(params)

    print(
        "Привет. Выберите, что хотите увидеть:\n"
        "1 - список всех компаний и количество вакансий у каждой компании.\n"
        "2 - список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n"
        "3 - среднюю зарплату по вакансиям\n"
        "4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n"
        "5 - список всех вакансий, в названии которых содержатся переданные в метод слова, например python."
    )

    user_input = input("Введите число: ")
    if user_input == 1:
        companies_and_vacancies_count = db_manager.get_company_and_vacancies_count()
        print(
            f"Список всех компаний и количество вакансий у каждой компании {companies_and_vacancies_count}"
        )

    elif user_input == 2:
        all_vacancies = db_manager.get_vacancies()
        print(
            f"Список всех вакансий "
            f"с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию {all_vacancies}"
        )

    elif user_input == 3:
        avg_salary = db_manager.get_avg_salary()
        print(f"Среднюю зарплату по вакансиям {avg_salary}")

    elif user_input == 4:
        vacancy_salary = db_manager.get_vacancies_with_salary()
        print(
            f"Список всех вакансий, у которых зарплата выше средней по всем вакансиям {vacancy_salary}"
        )

    elif user_input == 5:
        vacancy_with_keyword = db_manager.get_vacancies_for_keyword(
            conn=psycopg2.connect(dbname="hh", **params), keyword="Флорист"
        )

        for vacancy in vacancy_with_keyword:
            print(
                f"Список всех вакансий,"
                f" в названии которых содержатся переданные в метод слова, например python {vacancy}"
            )
    else:
        print("Не верный запрос")


if __name__ == "__main__":
    main()
