from sqlalchemy import Column, Integer, String, Numeric, SmallInteger, Date, ForeignKey, BigInteger, CHAR
from sqlalchemy.orm import relationship
from src.database.database import Base

class Operadora(Base):
    __tablename__ = "operadoras"

    reg_ans = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(14), unique=True, nullable=False)
    razao_social = Column(String(255), nullable=False)
    nome_fantasia = Column(String(255))
    modalidade = Column(String(100))
    logradouro = Column(String(255))
    numero = Column(String(20))
    complemento = Column(String(255))
    bairro = Column(String(150))
    cidade = Column(String(150))
    uf = Column(CHAR(2))
    cep = Column(String(8))
    ddd = Column(String(3))
    telefone = Column(String(20))
    fax = Column(String(20))
    endereco_eletronico = Column(String(255))
    representante = Column(String(255))
    cargo_representante = Column(String(150))
    regiao_comercializacao = Column(Integer)
    data_registro_ans = Column(Date)

    despesas = relationship("DespesaConsolidada", back_populates="operadora")


class DespesaConsolidada(Base):
    __tablename__ = "despesas_consolidadas"

    id = Column(BigInteger, primary_key=True, index=True)
    reg_ans = Column(Integer, ForeignKey("operadoras.reg_ans"), nullable=False)
    trimestre = Column(SmallInteger, nullable=False)
    ano = Column(SmallInteger, nullable=False)
    valor_despesas = Column(Numeric(15, 2), nullable=False)

    operadora = relationship("Operadora", back_populates="despesas")


class DespesaAgregada(Base):
    __tablename__ = "despesas_agregadas"

    id = Column(BigInteger, primary_key=True, index=True)
    razao_social = Column(String(255), nullable=False)
    uf = Column(CHAR(2))
    total_despesas = Column(Numeric(18, 2))
    media_trimestral = Column(Numeric(18, 2))
    desvio_padrao = Column(Numeric(18, 2))