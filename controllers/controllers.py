from fastapi import APIRouter  #type: ignore
from models.models import ContaPagarReceberResponse
from typing import List
from decimal import Decimal


router = APIRouter(prefix="/contas")

@router.get("/", response_model=List[ContaPagarReceberResponse])
def listar_contas():
  return [
    ContaPagarReceberResponse(
      id=1,
      descricao="Aluguel",
      valor=Decimal(900),
      tipo="PAGAR"
    ),
    ContaPagarReceberResponse(
      id=2,
      descricao="Curso",
      valor=800.120,
      tipo="PAGAR"
    )
  ]
