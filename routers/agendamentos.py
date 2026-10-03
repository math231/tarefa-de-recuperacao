from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(prefix="/agendamentos", tags=["Agendamentos"])

@router.post("/", response_model=schemas.AgendamentoResponse, status_code=201)
def criar(dados: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    novo = models.Agendamento(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=List[schemas.AgendamentoResponse])
def listar(servico: Optional[str] = None, db: Session = Depends(get_db)):
    consulta = db.query(models.Agendamento)
    if servico:
        consulta = consulta.filter(models.Agendamento.servico == servico)
    return consulta.all()

@router.put("/{id}", response_model=schemas.AgendamentoResponse)
def atualizar(id: int, dados: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    item = db.query(models.Agendamento).filter(models.Agendamento.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    for campo, valor in dados.model_dump().items():
        setattr(item, campo, valor)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    item = db.query(models.Agendamento).filter(models.Agendamento.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    db.delete(item)
    db.commit()
    return {"mensagem": "Agendamento removido"}