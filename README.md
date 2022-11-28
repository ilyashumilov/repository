<h1 align="center">Statistics management system</h1>

Путь к автосгенерированной документации: `/docs`.

## Запуск проекта

docker-compose build
docker-compose up

## Обращения к API

### Отобразить все записи  `/retrieve_items`

Метод: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d '{"start": "2022-09-28", "end": "2022-09-28"}'
"<hostname>/retrieve_items"
```

Ответ:

```
[
  {
    "id": 15,
    "date": "2022-11-28",
    "views": 0,
    "clicks": 0,
    "cost": 0,
    "cpc": 0,
    "cpm": 0
  },
  {
    "id": 13,
    "date": "2022-10-28",
    "views": 0,
    "clicks": 0,
    "cost": 0,
    "cpc": 0,
    "cpm": 0
  },
]
```

### Создать новую запись `/create_item`

Метод: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d '{
  "date": "2022-11-28",
  "views": 0,
  "clicks": 0,
  "cost": 0
}'
"<hostname>/create_item"
```

Ответ:

```
[
  {
    "id": 0,
    "date": "2022-11-28",
    "views": 0,
    "clicks": 0,
    "cost": 0,
    "cpc": 0,
    "cpm": 0
  }
]
```

### Удалить все записи `/delete`

Метод: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
"<hostname>/delete"
```

Ответ:

```
'All Stat items have been deleted'
```