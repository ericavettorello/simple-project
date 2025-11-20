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
- `GET /date` - Возвращает текущую дату в различных форматах
- `GET /date/iso` - Возвращает дату в ISO формате (YYYY-MM-DD)
- `GET /date/formatted` - Возвращает дату в читаемом формате с детальной информацией
- `GET /doc` - Редирект на `/docs`
- `GET /docs` - Интерактивная документация Swagger UI
- `GET /redoc` - Альтернативная документация ReDoc

## Пример использования

### Получить время сервера:
```bash
curl http://127.0.0.1:9000/time
```

Ответ:
```json
{
  "server_time": "2024-01-15T14:30:45.123456",
  "timestamp": "1705327845.123456",
  "formatted_time": "2024-01-15 14:30:45"
}
```

### Получить дату:
```bash
curl http://127.0.0.1:9000/date
```

Ответ:
```json
{
  "date": "2024-01-15",
  "date_iso": "2024-01-15",
  "date_formatted": "15.01.2024",
  "day": "Monday",
  "day_ru": "Понедельник"
}
```

### Получить дату в ISO формате:
```bash
curl http://127.0.0.1:9000/date/iso
```

### Получить дату в читаемом формате:
```bash
curl http://127.0.0.1:9000/date/formatted
```

(Или используйте порт, на котором запущен сервер)

