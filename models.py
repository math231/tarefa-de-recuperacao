from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, nullable=False)
    servico = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    horario = Column(String, nullable=False)
    concluido = Column(Boolean, default=False)