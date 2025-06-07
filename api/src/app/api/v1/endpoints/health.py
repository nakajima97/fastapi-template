from fastapi import APIRouter, Depends, HTTPException

from ...deps import get_health_service
from ....services.health_service import HealthService

router = APIRouter()


@router.get("/health/db")
async def health_check_db(
    health_service: HealthService = Depends(get_health_service)
):
    """
    データベースへの疎通確認用ヘルスチェックエンドポイント
    """
    result = await health_service.check_database_health()
    
    if result["status"] == "unhealthy":
        raise HTTPException(
            status_code=503,
            detail=result
        )
    
    return result 