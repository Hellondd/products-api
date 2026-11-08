# Products API

Учебный проект: каталог товаров на FastAPI.

## Задача

Реализовать CRUD для таблицы `products`:

- `id`
- `name` (строка, 2–80 символов, уникальное)
- `price` (целое, >= 0)
- `in_stock` (bool, по умолчанию True)

Эндпоинты: `POST /products`, `GET /products`, `GET /products/{id}`, `PUT /products/{id}`, `DELETE /products/{id}`.