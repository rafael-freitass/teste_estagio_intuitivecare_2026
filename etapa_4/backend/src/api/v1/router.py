from fastapi import APIRouter

from .routes.operadoras import router as operadoras_router
from .routes.estatisticas import router as estatisticas_router

api_router = APIRouter()

api_router.include_router(operadoras_router, prefix="/operadoras", tags=["Operadoras"])
api_router.include_router(estatisticas_router, prefix="/estatisticas", tags=["Estatísticas"])