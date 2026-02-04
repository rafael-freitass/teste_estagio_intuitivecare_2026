from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_

from src.database.database import get_db
from src.models.models import Operadora, DespesaConsolidada
from src.schemas.schemas import (
    OperadoraResponse,
    DespesaConsolidadaResponse,
    PaginatedOperadoras
)

router = APIRouter()


@router.get("/", response_model=PaginatedOperadoras)
def listar_operadoras(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    search: str = Query("", description="Busca por razão social ou CNPJ"),
    db: Session = Depends(get_db)
):

    offset = (page - 1) * limit

    query = db.query(Operadora)

    if search:
        query = query.filter(
            or_(
                Operadora.razao_social.ilike(f"%{search}%"),
                Operadora.cnpj.ilike(f"%{search}%")
            )
        )

    total = query.count()

    operadoras = (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )

    return {
        "data": operadoras,
        "total": total,
        "page": page,
        "limit": limit
    }


@router.get("/{cnpj}", response_model=OperadoraResponse)
def obter_operadora(cnpj: str, db: Session = Depends(get_db)):

    operadora = (
        db.query(Operadora)
        .filter(Operadora.cnpj == cnpj)
        .first()
    )

    if not operadora:
        raise HTTPException(404, "Operadora não encontrada")

    return operadora


@router.get("/{cnpj}/despesas", response_model=list[DespesaConsolidadaResponse])
def despesas_operadora(cnpj: str, db: Session = Depends(get_db)):

    operadora = (
        db.query(Operadora)
        .filter(Operadora.cnpj == cnpj)
        .first()
    )

    if not operadora:
        raise HTTPException(404, "Operadora não encontrada")

    despesas = (
        db.query(DespesaConsolidada)
        .filter(DespesaConsolidada.reg_ans == operadora.reg_ans)
        .all()
    )

    return despesas