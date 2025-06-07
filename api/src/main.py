from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from src.db import get_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health/db")
def health_check_db(db: Session = Depends(get_db)):
    """
    データベースへの疎通確認用ヘルスチェックエンドポイント
    """
    try:
        # シンプルなクエリを実行してDB接続を確認
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
            "message": "Database connection is working"
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "database": "disconnected",
                "message": f"Database connection failed: {str(e)}"
            }
        )
