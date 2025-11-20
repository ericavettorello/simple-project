from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from datetime import datetime
from typing import Dict, Any

app = FastAPI(title="Server Time API", version="1.0.0")


@app.get("/")
async def root() -> Dict[str, Any]:
    """Главная страница API"""
    return {
        "message": "Server Time API",
        "endpoints": {
            "/time": "Получить текущее время сервера",
            "/date": "Получить текущую дату",
            "/date/iso": "Получить дату в ISO формате",
            "/date/formatted": "Получить дату в читаемом формате",
            "/docs": "Интерактивная документация Swagger"
        }
    }


@app.get("/doc")
async def redirect_doc():
    """Редирект с /doc на /docs"""
    return RedirectResponse(url="/docs")


@app.get("/time")
async def get_server_time() -> Dict[str, str]:
    """Возвращает текущее время сервера"""
    current_time = datetime.now()
    return {
        "server_time": current_time.isoformat(),
        "timestamp": str(current_time.timestamp()),
        "formatted_time": current_time.strftime("%Y-%m-%d %H:%M:%S")
    }


@app.get("/date")
async def get_date() -> Dict[str, str]:
    """Возвращает текущую дату в различных форматах"""
    current_date = datetime.now()
    return {
        "date": current_date.strftime("%Y-%m-%d"),
        "date_iso": current_date.date().isoformat(),
        "date_formatted": current_date.strftime("%d.%m.%Y"),
        "day": current_date.strftime("%A"),
        "day_ru": {
            "Monday": "Понедельник",
            "Tuesday": "Вторник",
            "Wednesday": "Среда",
            "Thursday": "Четверг",
            "Friday": "Пятница",
            "Saturday": "Суббота",
            "Sunday": "Воскресенье"
        }.get(current_date.strftime("%A"), current_date.strftime("%A"))
    }


@app.get("/date/iso")
async def get_date_iso() -> Dict[str, str]:
    """Возвращает текущую дату в ISO формате (YYYY-MM-DD)"""
    current_date = datetime.now()
    return {
        "date": current_date.date().isoformat(),
        "format": "ISO 8601 (YYYY-MM-DD)"
    }


@app.get("/date/formatted")
async def get_date_formatted() -> Dict[str, str]:
    """Возвращает текущую дату в читаемом формате"""
    current_date = datetime.now()
    return {
        "date_formatted": current_date.strftime("%d.%m.%Y"),
        "date_long": current_date.strftime("%d %B %Y"),
        "date_short": current_date.strftime("%d/%m/%Y"),
        "day_name": current_date.strftime("%A"),
        "day_number": current_date.strftime("%d"),
        "month_name": current_date.strftime("%B"),
        "month_number": current_date.strftime("%m"),
        "year": current_date.strftime("%Y")
    }

