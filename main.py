from fastapi import FastAPI
from database import engine, Base
import models
from routers import agendamentos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Barbearia")
app.include_router(agendamentos.router)