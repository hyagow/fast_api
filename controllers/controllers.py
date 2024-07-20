from fastapi import APIRouter  #type: ignore
from models.models import ContaPagarReceberResponse
from typing import List
from decimal import Decimal


router = APIRouter(prefix="/contas")

db_conta = [
  {"id": 1, "descricao": "Aluguel", "valor": 900, "tipo": "PAGAR"},
  {"id": 2, "descricao": "Curso", "valor": 800.20, "tipo": "PAGAR"},
]

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

# @router.get("/", response_model=List[ContaPagarReceberResponse])
# def listar_uma_conta(conta_id: int):
#   for key, value in 
#   if conta_id == id.ContaPagarReceberResponse:
#     return [ContaPagarReceberResponse]
#   else:
#     raise ValueError("Item not found")

@router.post("/", response_model=ContaPagarReceberResponse)
def post_conta(id: int, descricao: str, valor: Decimal, tipo: str):
  if not id or not descricao or not valor or not tipo:
    raise ValueError("Produto não sem nome ou preço")
  return f'Item inserted successfully: {\
    "id": id, \
    "descricao": descricao, \
    "valor": valor, \
    "tipo": tipo
    }'

@router.put("/", response_model=ContaPagarReceberResponse)
def update_conta(conta_id: int):
  if conta_id >= len(db_conta):
    raise ValueError("Conta não encontrada")
  return db_conta[conta_id]