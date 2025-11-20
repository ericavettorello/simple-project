# Server Time API

Простое FastAPI приложение, возвращающее текущее время сервера.

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск

Запустите сервер с помощью uvicorn:

```bash
uvicorn main:app --reload --port 9000
```

Сервер будет доступен по адресу: http://127.0.0.1:9000

**Если порт 9000 занят**, запустите на другом свободном порту:

```bash
uvicorn main:app --reload --port 7000
```

## Запуск с Docker

**Важно:** Docker Desktop должен быть запущен перед выполнением команд.

### Как запустить Docker Desktop на Windows:

1. Найдите "Docker Desktop" в меню Пуск или на рабочем столе
2. Запустите приложение Docker Desktop
3. Дождитесь полной загрузки (иконка Docker в системном трее перестанет мигать)
4. Проверьте статус Docker:

```bash
docker --version
docker ps
```

Если команда `docker ps` выполняется без ошибок, Docker Desktop готов к работе.

Соберите Docker образ (не забудьте точку в конце):

```bash
docker build -t server-time-api .
```

Запустите контейнер:

```bash
docker run -p 9000:9000 server-time-api
```

Сервер будет доступен по адресу: http://127.0.0.1:9000

**Примечание:** Если вы видите ошибку `The system cannot find the file specified` или `dockerDesktopLinuxEngine`, убедитесь, что Docker Desktop запущен и работает.

## API Endpoints

- `GET /` - Главная страница с информацией об API
- `GET /time` - Возвращает текущее время сервера
- `GET /docs` - Интерактивная документация Swagger UI
- `GET /redoc` - Альтернативная документация ReDoc

## Пример использования

```bash
curl http://127.0.0.1:9000/time
```

(Или используйте порт, на котором запущен сервер)

Ответ:
```json
{
  "server_time": "2024-01-15T14:30:45.123456",
  "timestamp": 1705327845.123456,
  "formatted_time": "2024-01-15 14:30:45"
}
```

