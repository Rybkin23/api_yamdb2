## Проект YaMDB
«YaMDB» — проект на Django Rest Framework. 
# Описание:
Это учебный проект Яндекс.Практикум по API.
В этом проекте реализован backend API для сервиса по сбору отзывов на различные произведения.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
*здесь написать что может делать апи

# Пример запроса к API:

## Получение списка всех произведений

Получить список всех объектов. Права доступа: Доступно без токена.

Отправить GET-запрос на эндпоинт api/v1/titles/
### Пример ответа
```
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
```

## Добавление нового отзыва

Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение. Права доступа: Аутентифицированные пользователи.

Отправить POST-запрос на эндпоинт api/v1/titles/{title_id}/reviews/
### Пример запроса 
```
{
  "text": "string",
  "score": 1
}
```
### Пример ответа
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/BaldiskA/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
