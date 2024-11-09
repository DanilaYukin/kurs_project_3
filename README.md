# HH-parser — приложение для получения вакансий с сайта hh.ru и их обработки от определенных компаний 

## Описание:

Приложение позволяет позволяет получить интересующих вас работодателей и сохранить их в таблицу.
Также приложение позволяет получить данные о вакансиях от ваших работодателей и сохранить в таблицу.

## Установка:

Рекомендуется использовать PyCharm

Ссылка для добавления проекта
https://github.com/DanilaYukin/kurs_project_3

Для создания виртуального окружения и установки зависимостей используйте Poetry

Модуль `hh_api.py` использует сервис https://api.hh.ru/vacancies

## Использование:

Точкой запуска программы является модуль `main.py` - просто запустите его

## Функционал

Функционал содержится в 4-ех модулях

Модули:
1. `hh_api` - основной функциональный модуль для работы с внешним сервисом
2. `db` - модуль для подключение к базе данных, созданию таблиц и сохранению в них данных
3. `DBManager` - модуль для получения вакансий которые вас интересуют
4. `config` - модуль для получение праметров подключение к базе данных

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE)