from enum import Enum
from pydantic import BaseModel, Field


class HealthStatus(str, Enum):
    """ヘルスステータスの列挙型"""
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"


class DatabaseStatus(str, Enum):
    """データベースステータスの列挙型"""
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"


class DatabaseHealthResponse(BaseModel):
    """データベースヘルスチェックのレスポンスモデル"""
    status: HealthStatus = Field(
        ...,
        description="ヘルスチェックの結果ステータス",
        example="healthy"
    )
    database: DatabaseStatus = Field(
        ...,
        description="データベース接続の状態",
        example="connected"
    )
    message: str = Field(
        ...,
        description="ヘルスチェックの詳細メッセージ",
        example="Database connection is working"
    )
    
    class Config:
        """Pydanticの設定"""
        schema_extra = {
            "example": {
                "status": "healthy",
                "database": "connected",
                "message": "Database connection is working"
            }
        } 