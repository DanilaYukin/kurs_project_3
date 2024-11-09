import psycopg2


class DB:
    """"""

    def __init__(self, host: str, database: str, user: str, password: str):
        self.conn = psycopg2.connect(host=host, database=database, user=user, password=password)

    def create_table(self):
        with self.conn.cursor() as cur:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS employer (
                employer_id int PRIMARY KEY, 
                employer_name varchar(200),
                employer_url varchar(100))"""
            )
            self.conn.commit()
        with self.conn.cursor() as cur:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS vacancies (
                vacancy_id int, 
                vacancy_name varchar(200),
                salary int,
                vacancy_url varchar(100),
                employer_id int,
                CONSTRAINT fk_vacancies_employer_id FOREIGN KEY(employer_id) REFERENCES employer(employer_id))"""
            )
            self.conn.commit()

    def save_data_employer(self, data):
        with self.conn.cursor() as cur:
            for emp in data:
                employer_id = emp['id']
                employer_name = emp['name']
                employer_url = emp['url']
                cur.execute(
                    """INSERT INTO employer(employer_id, name, url)
                    VALUES (%s, %s, %s)
                    """,
                    (employer_id, employer_name, employer_url)
                )
                self.conn.commit()

    def save_data_vacancies(self, data):
        with self.conn.cursor() as cur:
            for vac in data:
                cur.execute(
                    """INSERT INTO vacancies(vacancy_id, name, salary, url, employer_id)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (vac['id'],
                     vac['name'],
                     vac['salary']['from'],
                     vac['url'],
                     vac['employer_id']['id']
                     )
                )
            self.conn.commit()


if __name__ == "__main__":
    db = DB(host='localhost', database='kurs_project_3', user='postgres', password='fiatducato495')
    print(db.create_table())
