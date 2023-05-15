# Техническое задание
Необходимо разработать:  
Client для работы с Teachbase API. 
1. Авторизация.
2. Проверка токена.
3. Отправка запросов.         
4. Реализовать в клиенте методы для получения/отправки данных из (в) Teachbase API (POST, GET). 
https://go.teachbase.ru/api-docs/index.html#/courses/get_courses - список курсов
https://go.teachbase.ru/api-docs/index.html#/courses/get_courses__id_ - детальное представление курса
https://go.teachbase.ru/api-docs/index.html#/users/post_users_create - создание пользователя
https://go.teachbase.ru/api-docs/index.html#/course_sessions/post_course_sessions__session_id__register - запись пользователя на сессию
https://go.teachbase.ru/api-docs/index.html#/course_sessions/get_courses__course_id__course_sessions - сессии курсов
5. Создать модель курса с сохранение данных из Teachbase (*).
6. DRF. Реализовать метод для получения данных курса из модели Django (*).
Список всех курсов - /courses/   
Детальное представление курса - /courses/<id>

### Flow проверки задания:
1. Создаём пользователя.
2. Получаем список курсов и сессии курсов.
3. Записываем юзера на сессию.
4. Проверяем.

### Необходимые материалы:

- Swagger Teachbase
https://go.teachbase.ru/api-docs/index.html

- OAuth application
Public key 8bdf8070ca5eb1ee7565aa4722e9772a60612310f62f0a04ba4774e7527c836b
Secret key c2c76197cc8de37d0d04a9cc4127ef7bb5c0961d4f96eeec6fff403e30b304dd

- Предпочитаемый стек (минимум описан ниже):
Django 4, DRF, Postgres.
