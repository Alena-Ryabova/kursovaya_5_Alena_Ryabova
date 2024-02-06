from src.DBManager import DBManager
from vacancies_hh import VacancyHh

if __name__ == "__main__":
    # Создаем экземпляр класса DBManager
    db_manager = DBManager()

    # Создаем таблицу
    db_manager.create_table()

    # Создаем экземпляр класса VacancyHh
    vacancy_hh_instance = VacancyHh()

    # Получаем вакансии для нескольких работодателей
    employer_ids = ['9498120', '561525', '4237294', '84585', '155416', '2661230', '1455',
                    '2324020', '4619258', '632253', '1551422', '5875196', '3590333', '3096092', '839098']
    vacancies = vacancy_hh_instance.get_vacancies_for_multiple_employers(employer_ids)

    # Вставляем вакансии в таблицу
    if vacancies:
        db_manager.insert_vacancies(vacancies)
        db_manager.get_companies_and_vacancies_count()
        db_manager.get_all_vacancies()
        db_manager.get_avg_salary()
        db_manager.get_vacancies_with_higher_salary()
        user_keyword = input("Ввести ключевое слово \n")
        db_manager.get_vacancies_with_keyword(user_keyword)
    else:
        print("Не удалось получить вакансии.")

    # Закрываем соединение
    db_manager.conn.close()


