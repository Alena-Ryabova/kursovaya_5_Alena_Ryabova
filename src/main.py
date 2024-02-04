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
    employer_ids = ['9498120', '9508647', '4237294', '3976542', '155416',
                    '1426733', '6068238', '632253', '1551422', '5875196']
    vacancies = vacancy_hh_instance.get_vacancies_for_multiple_employers(employer_ids)

    # Вставляем вакансии в таблицу
    if vacancies:
        db_manager.insert_vacancies(vacancies)
    else:
        print("Не удалось получить вакансии.")

    # Закрываем соединение
    db_manager.conn.close()


