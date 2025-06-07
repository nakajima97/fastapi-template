from fastapi import Depends
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..services.health_service import HealthService


def get_health_service(db: Session = Depends(get_db)) -> HealthService:
    """HealthServiceの依存性注入"""
    return HealthService(db) 