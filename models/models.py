from pydantic import BaseModel, Field
from decimal import Decimal

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
