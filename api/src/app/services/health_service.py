from sqlalchemy.orm import Session
from sqlalchemy import text


class HealthService:
    """ヘルスチェック関連のビジネスロジック"""

    def __init__(self, db: Session):
        self.db = db

    async def check_database_health(self) -> dict:
        """
        データベースの健全性をチェック
        
        Returns:
            dict: ヘルスチェック結果
        """
        try:
            # シンプルなクエリを実行してDB接続を確認
            self.db.execute(text("SELECT 1"))
            return {
                "status": "healthy",
                "database": "connected",
                "message": "Database connection is working",
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "database": "disconnected", 
                "message": f"Database connection failed: {str(e)}",
            } 