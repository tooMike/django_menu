# Описание

Реализовано приложение Django, которое позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.  `{% draw_menu 'main_menu' %}`

# Авторы проекта

[Mikhail](https://github.com/tooMike)

# Установка и запуск с Docker

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/tooMike/django_menu
```

```
cd django_menu
```

Запустить сборку проекта:

```
docker compose up
```

Выполнить сбор статики в контейнере backend:

```
docker compose exec backend python manage.py collectstatic
```

Выполнить миграции в контейнере backend:

```
docker compose exec backend python manage.py migrate
```

Проект будет доступен по адресу

```
http://127.0.0.1:8000/
```

# Добавление тестовых данных (пользователи, ингредиенты, теги, рецепты)

Выполнить команду import_data в контейнере backend:

```
docker compose exec backend python manage.py create_test_menus
```