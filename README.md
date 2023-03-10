# Grocery Shop

## Запуск
```bash
pip install requirements.txt
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
## Навигация
* Тесты можно найти по следующему пути [test_api.py](job%2Ftests%2Ftest_api.py)
  * для тестов использовался стек PyTest + Factoryboy + Faker
* Эндпоинты обрабатываются здесь [views.py](job%2Fviews.py)

## Endpoints
Для использования потребуется создать хотя бы 1 экземпляр Resume. (в админке, например)
* GET (ALL) : /resume
* PATCH (STAFF): /resume/{int:pk}