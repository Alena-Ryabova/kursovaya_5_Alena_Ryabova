import psycopg2


class DBManager():

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="Kurs_5",
            user="postgres",
            password="325896325896"
        )

    def create_table(self):
        with self.conn.cursor() as cur:
            create_table_query = """
               CREATE TABLE IF NOT EXISTS vacancies (
                   id SERIAL PRIMARY KEY,
                   name VARCHAR(255),
                   employer VARCHAR(255),
                   employer_id VARCHAR(50),
                   vacancy_url VARCHAR(255),
                   salary INTEGER
               );
               """
            cur.execute(create_table_query)
            self.conn.commit()

    def insert_vacancies(self, vacancies):
        with self.conn.cursor() as cur:
            for vacancy in vacancies:
                insert_query = """
                   INSERT INTO vacancies (name, employer, employer_id, vacancy_url, salary)
                   VALUES (%s, %s, %s, %s, %s);
                   """

                salary_data = vacancy.get('salary', {})
                salary_value = salary_data.get('from') if salary_data and salary_data.get('from') is not None else 0
                data = (
                    vacancy.get('name', ''),
                    vacancy.get('employer', {}).get('name', ''),
                    vacancy.get('employer', {}).get('id', ''),
                    vacancy.get('alternate_url', ''),
                    salary_value
                )
                cur.execute(insert_query, data)

            self.conn.commit()
            print(f"Данные успешно загружены в таблицу.")

    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании. 

        """
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT employer, COUNT(*) "
                        f"FROM vacancies "
                        f"GROUP BY employer "
                        f"ORDER BY COUNT(*);")
            self.conn.commit()

            result = cur.fetchall()
            print(f"\nПолучен список всех компаний и количество вакансий у каждой компании.")
            print(result)
        return result

    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию. 

        """

        with self.conn.cursor() as cur:
            cur.execute(f"SELECT name, employer, salary, vacancy_url "
                        f"FROM vacancies; ")
            self.conn.commit()

            result = cur.fetchall()
            print(f"\nПолучен список всех вакансий с указанием названия компании,"
                  f"названия вакансии и зарплаты и ссылки на вакансию.")
            print(result)
        return result

    def get_avg_salary(self):
        """
        получает среднюю зарплату по вакансиям. 

        """

        with self.conn.cursor() as cur:
            cur.execute(f"SELECT AVG(salary) FROM vacancies; ")
            self.conn.commit()

            result = cur.fetchall()
            print(f"\nПолучена средняя зарплата по вакансиям.")
            print(result)
        return result

    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям. 

        """

        with self.conn.cursor() as cur:
            cur.execute(f"SELECT name FROM vacancies "
                        f"WHERE salary > (SELECT AVG(salary) FROM vacancies); ")
            self.conn.commit()

            result = cur.fetchall()
            print(f"\nПолучен список всех вакансий, у которых зарплата выше средней по всем вакансиям.")
            print(result)
        return result

    def get_vacancies_with_keyword(self, keyword):
        """
        получает список всех вакансий,
        в названии которых содержатся переданные в метод слова, например python

        """

        with self.conn.cursor() as cur:
            search_query = """
                            SELECT * FROM vacancies WHERE LOWER(name) LIKE %s;
                        """
            cur.execute(search_query, ('%' + keyword.lower() + '%',))
            self.conn.commit()

            result = cur.fetchall()
            print(f"\nПолучен список всех вакансий, "
                  f"в названии которых содержатся переданные в метод слова, например 'удаленно'. ")
            print(result)
        return result
