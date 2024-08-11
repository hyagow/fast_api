from pydantic import BaseModel, Field
from decimal import Decimal
from sqlalchemy import Column, Integer, String, Float
from db.database import Base


# Model to Response
class ContaPagarReceberResponse(BaseModel):
  id: int
  descricao: str
  valor: float | Decimal=Field(..., description="Valor da conta")
  tipo: str

# Model to Request
class ContaPagarReceberRequest(BaseModel):
  descricao: str
  valor: float | Decimal=Field(..., description="Valor da conta")
  tipo: str

# Model to Conta in database
class Contas(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)
    valor = Column(Float)
    tipo = Column(String, index=True)