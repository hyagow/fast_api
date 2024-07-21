from pydantic import BaseModel, Field
from decimal import Decimal

class ContaPagarReceberResponse(BaseModel):
  id: int
  descricao: str
  valor: float | Decimal=Field(..., description="Valor da conta", example='100.40')
  tipo: str


class ContaPagarReceberRequest(BaseModel):
  descricao: str
  valor: float | Decimal=Field(..., description="Valor da conta", example='100')
  tipo: str
