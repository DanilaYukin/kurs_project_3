import psycopg2


class DBManager:

    def __init__(self, params):
        self.conn = psycopg2.connect(dbname="hh", **params)
        self.cur = self.conn.cursor()

    def get_company_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        self.cur.execute(
            """
        SELECT employer.employer_name, COUNT(vacancies.employer_id)
        FROM employers
        JOIN vacancy ON employer.employer_id = vacancies.employer_id
        GROUP BY employer.employer_name
        ORDER BY COUNT(vacancies.employer_id) DESC;"""
        )

        return self.cur.fetchall()

    def get_vacancies(self):
        """получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""
        self.cur.execute(
            """
        SELECT employer.employer_name, vacancy_name, salary, vacancy_url
        FROM vacancy
        JOIN employer ON employer.employer_id = vacancy.employer_id
        ORDER BY salary DESC;"""
        )

        return self.cur.fetchall()

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        self.cur.execute(
            """
        SELECT AVG(salary) FROM vacancy;"""
        )

        return self.cur.fetchall()

    def get_vacancies_with_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        self.cur.execute(
            """
        SELECT vacancy_name, salary 
        FROM vacancy
        WHERE salary > (SELECT AVG(salary) FROM vacancy);"""
        )

        return self.cur.fetchall()

    def get_vacancies_for_keyword(self, conn, keyword):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        with self.conn.cursor() as self.cur:
            query = """SELECT * FROM vacancy WHERE vacancy_name LIKE %s"""

            self.cur.execute(query, (f"%{keyword}%",))

            return self.cur.fetchall()
