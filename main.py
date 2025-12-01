import time
import random
import requests
import json
import os
from dataclasses import dataclass, asdict
import signal


HH_API_URL = 'https://api.hh.ru/vacancies'


@dataclass
class Vacancy:
    name: str
    salary: str
    link: str


def retry_decorator(func):
    def wrapper(*args, **kwargs):
        response = None
        for _ in range(3):
            response = func(*args, **kwargs)
            if response:
                break
            else:
                time.sleep(random.uniform(2, 3))
                continue
        return response
    return wrapper


@retry_decorator
def fetch_vacancies_on_page(text:str,
                            per_page: int,
                            page: int):

    print(f'{page}.Делаем запрос на api hh')

    url = HH_API_URL + f'?text={text}&per_page={per_page}&page={page}'

    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        print('Запрос не прошел, делаем повторный через 2 секунды')
        return None
    else:
        result = response.json()
        return result


def fetch_all_vacancies():

    text = 'FastApi'
    per_page = 100
    page = 0

    while True:

        result = fetch_vacancies_on_page(text, per_page, page)
        if result['items']:

            try:
                with open('vacancies.json', 'a', encoding='utf-8') as file:
                    vacancies = result['items']

                    for vacancy in vacancies:
                        vacancy_obj = Vacancy(
                            vacancy['name'],
                            vacancy['salary'],
                            vacancy['alternate_url'],
                        )
                        json.dump(asdict(vacancy_obj),
                                  file,
                                  ensure_ascii=False,
                                  indent=4)
                        file.write('\n')

                time.sleep(random.uniform(1, 2))
                print('Успешно!')

            except KeyError:
                time.sleep(random.uniform(1, 2))
                print('Ошибка ключа при извлечении данных!')

            page += 1
            if page == 20:
                break

        else:
            print('Больше нет данных по вакансиям!')
            break

def delete_previous_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

def _timeout_handler(signum, frame):
    raise TimeoutError("Функция превысила лимит времени")


def main():
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(150)
    try:
        delete_previous_file(filename='vacancies.json')
        fetch_all_vacancies()
    finally:
        signal.alarm(0)


if __name__ == '__main__':
    main()