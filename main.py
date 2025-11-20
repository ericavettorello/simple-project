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

