from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from src.database.database import get_db
from src.models.models import DespesaConsolidada, Operadora

router = APIRouter()


@router.get("/")
def estatisticas(db: Session = Depends(get_db)):

    total = db.query(func.sum(DespesaConsolidada.valor_despesas)).scalar()
    media = db.query(func.avg(DespesaConsolidada.valor_despesas)).scalar()

    top5 = (
        db.query(
            DespesaConsolidada.reg_ans,
            func.sum(DespesaConsolidada.valor_despesas).label("total")
        )
        .group_by(DespesaConsolidada.reg_ans)
        .order_by(func.sum(DespesaConsolidada.valor_despesas).desc())
        .limit(5)
        .all()
    )

    return {
        "total_despesas": float(total or 0),
        "media_despesas": float(media or 0),
        "top5_operadoras": [
            {"reg_ans": t.reg_ans, "total": float(t.total)}
            for t in top5
        ]
    }


@router.get("/despesas-por-uf")
def despesas_por_uf(db: Session = Depends(get_db)):

    resultado = (
        db.query(
            Operadora.uf,
            func.sum(DespesaConsolidada.valor_despesas).label("total")
        )
        .join(
            Operadora,
            Operadora.reg_ans == DespesaConsolidada.reg_ans
        )
        .group_by(Operadora.uf)
        .order_by(func.sum(DespesaConsolidada.valor_despesas).desc())
        .all()
    )

    return [
        {
            "uf": r.uf,
            "total": float(r.total or 0)
        }
        for r in resultado
    ]