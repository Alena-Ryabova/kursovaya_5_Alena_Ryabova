import requests


class VacancyHh():
    """
    Класс для работы с hh.ru
    """
    url = "https://api.hh.ru/vacancies"

    def get_vacancies_by_employer(self, employer_id):
        """Метод получает вакансии,
         найденные по ключевому слову
         """

        params = {
            "area": 113,  # Код региона 113-Россия
            'employer_id': employer_id,
            "per_page": 30  # Количество вакансий на странице
        }
        try:
            response_hh = requests.get(url=self.url, params=params,
                                       headers={'User-Agent': 'YourApp/1.0 (alena1987.12@gmail.com)'})
            if response_hh.status_code == 200:
                data = response_hh.json()
                vacancies = data['items']
                return vacancies

        except requests.RequestException as error:
            print(f'Ошибка при получении данных. {error}')
            return None

    def get_vacancies_for_multiple_employers(self, employer_ids):
        all_vacancies = []

        for employer_id in employer_ids:
            vacancies = self.get_vacancies_by_employer(employer_id)
            if vacancies:
                all_vacancies.extend(vacancies)

        return all_vacancies
