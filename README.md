# Advert-Project

## API веб-приложения для создания объявлений о безвозмездной передаче вещей.

### Запуск с помощью docker-compose
Для запуска приложения необходимо:
1. перейти в папку mytestprj
2. выполнить команду docker-compose.up
3. выполнить команду docker-compose exec web bash
4. выполнить команду python manage.py makemigrations
5. выполнить команду python manage.py migrate
6. выполнить команду python manage.py createsuperuser


   *перейти по адресу http://127.0.0.1:8000/admin/ - для входа в кабинет администратора
   *перейти по адресу http://127.0.0.1:8000/api/schema/swagger-ui/ - документация

### Запуск без docker
1. создать пустую папку
2. открыть командную строку, выполнить команду python -m venv venv
3. выполнить команду venv\Scripts\activate
4. склонировать в эту же папку проект с github
5. перейти в папку mytestprj/advert/advert/settings.py и установить необходимые параметры DATABASES (128 cтрочка кода)
6. перейти в папку mytestprj/advert
7. выполнить команду python manage.py makemigrations
8. выполнить команду python manage.py migrate
9. выполнить команду python manage.py createsuperuser

   
   перейти по адресу http://127.0.0.1:8000/admin/ - для входа в кабинет администратора
   перейти по адресу http://127.0.0.1:8000/api/schema/swagger-ui/ - документация


В админ-панели, нужно создайть пару категорий для товаров вручную. После чего можно проверить работу приложения.
