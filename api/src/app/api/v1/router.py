from fastapi import APIRouter

from .endpoints import health

api_router = APIRouter()

# ヘルスチェック関連のエンドポイント
api_router.include_router(health.router, tags=["health"]) 