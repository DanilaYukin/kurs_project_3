import requests


def get_employees():
    """
    Получаем 10 работодателей с HH.ру
    """
    url_hh = "https://api.hh.ru/vacancies"
    list_company = []
    params = {"currency": "RUR", "host": "hh.ru", "per_page": 100, "page": 0}
    while True:
        vacancies_hh = requests.get(
            url_hh, params=params).json()
        for vacancy in vacancies_hh["items"]:
            if vacancy["employer"].get("id"):
                company = {
                    "id": vacancy["employer"]["id"],
                    "name": vacancy["employer"]["name"],
                    "url": vacancy["employer"]["url"],
                }
                if company not in list_company:
                    list_company.append(company)
                if len(list_company) > 9:
                    break
                params["page"] += 1
        return list_company


def load_vacancies(list_company):
    """загрузка вакансий"""
    vacancy_info = []
    for employer_id in list_company:
        params = {"per_page": 10, "page": 0, "employer": employer_id["id"]}
        vacancy_url = "https://api.hh.ru/vacancies"
        response = requests.get(vacancy_url, params=params)
        vacancies = response.json()["items"]
        vacancy_info.extend(vacancies)
    vacancies_result = []
    for vacancy in vacancy_info:
        vacancy_full = {
            "name": vacancy['name'],
            "id": vacancy['id'],
            "salary": vacancy['salary'],
            "url": vacancy['url'],
            "employer_id": vacancy['employer']
        }
        if vacancy_full not in vacancies_result:
            vacancies_result.append(vacancy_full)
    return vacancies_result


if __name__ == "__main__":
    print(load_vacancies(get_employees()))
