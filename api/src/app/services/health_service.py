from sqlalchemy.orm import Session
from sqlalchemy import text

from ..schemas.health import DatabaseHealthResponse, HealthStatus, DatabaseStatus


class HealthService:
    """ヘルスチェック関連のビジネスロジック"""

    def __init__(self, db: Session):
        self.db = db

    async def check_database_health(self) -> DatabaseHealthResponse:
        """
        データベースの健全性をチェック
        
        Returns:
            DatabaseHealthResponse: ヘルスチェック結果
        """
        try:
            # シンプルなクエリを実行してDB接続を確認
            self.db.execute(text("SELECT 1"))
            return DatabaseHealthResponse(
                status=HealthStatus.HEALTHY,
                database=DatabaseStatus.CONNECTED,
                message="Database connection is working"
            )
        except Exception as e:
            return DatabaseHealthResponse(
                status=HealthStatus.UNHEALTHY,
                database=DatabaseStatus.DISCONNECTED,
                message=f"Database connection failed: {str(e)}"
            ) 