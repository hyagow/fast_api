from fastapi import APIRouter  #type: ignore
from models.models import ContaPagarReceberResponse, ContaPagarReceberRequest
from typing import List
# from decimal import Decimal


router = APIRouter(prefix="/contas")

# db_conta = [
#   {"id": 1, "descricao": "Aluguel", "valor": 900, "tipo": "PAGAR"},
#   {"id": 2, "descricao": "Curso", "valor": 800.20, "tipo": "PAGAR"},
# ]

@router.get("/", response_model=List[ContaPagarReceberResponse])
def listar_contas():
  return [
    ContaPagarReceberResponse(
      id=1,
      descricao="Aluguel",
      valor=1000,
      tipo="PAGAR"
    ),
    ContaPagarReceberResponse(
      id=2,
      descricao="Curso",
      valor=800.120,
      tipo="PAGAR"
    )
  ]

@router.post("/", response_model=ContaPagarReceberResponse, status_code=201)
def criar_conta(conta: ContaPagarReceberRequest):
  return ContaPagarReceberResponse(
    id=3,
    descricao=conta.descricao,
    valor=conta.valor,
    tipo=conta.tipo
  )



# @router.get("/", response_model=List[ContaPagarReceberResponse])
# def listar_uma_conta(conta_id: int):
#   for key, value in 
#   if conta_id == id.ContaPagarReceberResponse:
#     return [ContaPagarReceberResponse]
#   else:
#     raise ValueError("Item not found")

# @router.put("/", response_model=ContaPagarReceberResponse)
# def update_conta(conta_id: int):
#   if conta_id >= len(db_conta):
#     raise ValueError("Conta não encontrada")
#   return db_conta[conta_id]