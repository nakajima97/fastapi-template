from datetime import datetime
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
        ..., description="ヘルスチェックの結果ステータス", example="healthy"
    )
    database: DatabaseStatus = Field(
        ..., description="データベース接続の状態", example="connected"
    )
    message: str = Field(
        ...,
        description="ヘルスチェックの詳細メッセージ",
        example="Database connection is working",
    )

    class Config:
        """Pydanticの設定"""

        schema_extra = {
            "example": {
                "status": "healthy",
                "database": "connected",
                "message": "Database connection is working",
            }
        }


class DatabaseHealthErrorResponse(BaseModel):
    """データベースヘルスチェックエラー時のレスポンスモデル (HTTPException用)"""

    detail: dict = Field(
        ...,
        description="エラーの詳細情報",
        example={
            "status": "unhealthy",
            "database": "disconnected",
            "message": "Database connection failed: connection timeout",
        },
    )

    class Config:
        """Pydanticの設定"""

        schema_extra = {
            "example": {
                "detail": {
                    "status": "unhealthy",
                    "database": "disconnected",
                    "message": "Database connection failed: connection timeout",
                }
            }
        }


class ApplicationHealthResponse(BaseModel):
    """アプリケーションヘルスチェックのレスポンスモデル"""

    status: HealthStatus = Field(
        ..., description="アプリケーションのヘルスステータス", example="healthy"
    )
    application: str = Field(
        ..., description="アプリケーション名", example="FastAPI Template"
    )
    version: str = Field(..., description="アプリケーションバージョン", example="0.1.0")
    timestamp: datetime = Field(
        ..., description="ヘルスチェック実行時刻", example="2024-01-01T12:00:00.000Z"
    )
    message: str = Field(
        ...,
        description="ヘルスチェックメッセージ",
        example="Application is running successfully",
    )

    class Config:
        """Pydanticの設定"""

        schema_extra = {
            "example": {
                "status": "healthy",
                "application": "FastAPI Template",
                "version": "0.1.0",
                "timestamp": "2024-01-01T12:00:00.000Z",
                "message": "Application is running successfully",
            }
        }
