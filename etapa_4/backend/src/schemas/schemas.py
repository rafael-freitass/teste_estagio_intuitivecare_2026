from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from decimal import Decimal
from datetime import date


# ----------------------------
# Despesa Consolidada
# ----------------------------
class DespesaConsolidadaBase(BaseModel):
    reg_ans: int
    trimestre: int
    ano: int
    valor_despesas: Decimal


class DespesaConsolidadaResponse(DespesaConsolidadaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# ----------------------------
# Operadora
# ----------------------------
class OperadoraBase(BaseModel):
    reg_ans: int
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = None
    modalidade: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    data_registro_ans: Optional[date] = None


class OperadoraResponse(OperadoraBase):
    model_config = ConfigDict(from_attributes=True)


# ----------------------------
# Operadora com despesas
# ----------------------------
class OperadoraDetalhe(OperadoraResponse):
    despesas: List[DespesaConsolidadaResponse] = []


# ----------------------------
# Despesa Agregada
# ----------------------------
class DespesaAgregadaResponse(BaseModel):
    id: int
    razao_social: str
    uf: Optional[str] = None
    total_despesas: Optional[Decimal] = None
    media_trimestral: Optional[Decimal] = None
    desvio_padrao: Optional[Decimal] = None

    model_config = ConfigDict(from_attributes=True)


# ----------------------------
# Paginação Operadoras
# ----------------------------
class PaginatedOperadoras(BaseModel):
    data: List[OperadoraResponse]
    total: int
    page: int
    limit: int