# Web-приложение для определения заполненных форм.

Стек используемых технологий:
* Django
* Docker
* Docker-compose
* Mongodb

Описание.
В базе данных хранится список шаблонов форм. Шаблон формы, это структура, которая задается уникальным набором полей, с указанием их типов.
Так же все поля поддерживают валидацию. Принцип работы такой, что на вход по урлу /get_form POST запросом передаются данные такого вида:

```python
{
    f_name1=value1,
    f_name2=value2
}
```

В ответ возвращается список имен шаблонов форм, если они были найдены.
Подходящим шаблоном считается тот, поля которого совпали с полями в присланной форме и у которых совпали имя и тип значения. Полей в пришедшей форме может быть больше чем в шаблоне, в этом случае шаблон все равно будет считаться подходящим.

Если подходящей формы не нашлось, вернуть ответ в следующем формате
```json
{
    "f_name1": "FIELD_TYPE",
    "f_name2": "FIELD_TYPE"
}

```
где FIELD_TYPE это тип поля, выбранный на основе правил валидации.
Пример шаблона формы:

```json
{
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
}
```

Всего поддерживаться четыре типа данных полей: 
* email
* телефон
* дата
* текст

Все типы кроме текста должны поддерживать валидацию. Телефон передается в стандартном формате:
```python
+7 xxx xxx xx xx
```
дата передается в формате:
```python
YYYY-MM-DD.
```
В качестве базы данных используется Docker с MongoDB.

Инструкция по установке:

Скачайте данный и выполните команду:
```python
docker-compose up -d --build
```
После сборки контейнеров вы можете загрузить данные в бд. 
```python
docker-compose exec web python manage.py loaddata fixtures.json
```
В тестовой бд несколько форм и суперюзер: login: admin, password: admin.
После чего перейдите по адресу: http://127.0.0.1:8000/get_form/





