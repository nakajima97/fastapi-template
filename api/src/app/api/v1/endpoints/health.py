from fastapi import APIRouter, Depends, HTTPException

from ...deps import get_health_service
from ....services.health_service import HealthService

router = APIRouter()


@router.get(
    "/health/db",
    summary="Health Check DB",
    description="データベースへの疎通確認用ヘルスチェックエンドポイント"
)
async def health_check_database(
    health_service: HealthService = Depends(get_health_service)
):
    result = await health_service.check_database_health()
    
    if result["status"] == "unhealthy":
        raise HTTPException(
            status_code=503,
            detail=result
        )
    
    return result 