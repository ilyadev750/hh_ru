## Проект 1 hh.ru API
<p align="center">
  <img alt="Static Badge" src="https://img.shields.io/badge/python-3.11-blue">
  <img alt="Static Badge" src="https://img.shields.io/badge/requests-red">

## О проекте
Данный проект представляет собой скрипт, который извлекает данные об актуальных вакансиях с ресурса hh.ru через API
URL - solvit.space/projects/vacancies_statistics

## Особенности проекта

- запрос к API hh.ru реализован через retry декоратор
- скрипт будет работать только через ОС Mac/Linux, так как таймаут выполнения функции реализован через signal, который не работает на Windows
- если файл vacancies.json уже создан, то он будет удален при новом запуске программы и будет наполнен данными заново

## Как пользоваться приложением

- использовать ОС Mac/Ubuntu
- склонировать данный репозиторий
- установить виртуальное окружение Python версии 3.11
- в функции fetch_all_vacancies() задать параметр text(критерии поиска вакансии/должности)
- в терминале запустите скрипт python main.py
- после выполнения программы появиться файл vacancies.json
  

