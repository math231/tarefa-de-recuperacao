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