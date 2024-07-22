from fastapi import APIRouter, HTTPException, status
from models.models import ContaPagarReceberResponse, ContaPagarReceberRequest
from typing import List


router = APIRouter(prefix="/contas", tags=["Contas"])

db_contas = [
  {"id": 1, "descricao": "Aluguel", "valor": 900, "tipo": "PAGAR"},
  {"id": 2, "descricao": "Curso", "valor": 800.20, "tipo": "PAGAR"},
]

@router.get("/", response_model=List[ContaPagarReceberResponse])
def listar_contas() -> list:
  return db_contas

@router.get("/conta/{id}", response_model=ContaPagarReceberResponse, status_code=200)
def listar_uma_conta(conta_id: int) -> dict:
  for conta in db_contas:
    if conta["id"] == conta_id:
      return conta
  else:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Conta do id: {conta_id}, não foi localizada.')
  
@router.post("/", response_model=ContaPagarReceberResponse, status_code=201)
def criar_conta(conta: ContaPagarReceberRequest) -> dict:
  if conta:
    new_conta = {
      "id":len(db_contas)+1, 
      "descricao":conta.descricao,
      "valor":conta.valor,
      "tipo":conta.tipo    
      }
    db_contas.append(new_conta)
  return new_conta


@router.put("/conta/{id}", response_model=ContaPagarReceberRequest, status_code=200)
def atualizar_conta(conta_id: int, conta_update: ContaPagarReceberRequest) -> dict:
  for conta in db_contas:
    if conta["id"] == conta_id:
      conta["descricao"] = conta_update.descricao
      conta["valor"] = conta_update.valor
      conta["tipo"] = conta_update.tipo
      return conta
  else:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Conta do id: {conta_id}, não foi localizada.')

@router.delete("/conta/{id}", status_code=204)
def deletar_conta(conta_id: int):
  for conta in db_contas:
    if conta["id"] == conta_id:
      db_contas.remove(conta)
      return print(f'Conta do id: {conta_id}, foi deletada.')
  else:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Conta do id: {conta_id}, não foi localizada.')