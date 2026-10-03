from pydantic import BaseModel, ConfigDict

class AgendamentoBase(BaseModel):
    cliente: str
    servico: str
    preco: float
    horario: str
    concluido: bool = False

class AgendamentoCreate(AgendamentoBase):
    pass

class AgendamentoResponse(AgendamentoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)