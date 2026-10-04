# API da Barbearia 
Feito por:Matheus Elias da Silva Oliveira

API RESTful para gerenciar agendamentos de uma barbearia/salão de beleza, feita com **FastAPI**, **Pydantic** e **SQLAlchemy**, com banco de dados **SQLite**.

## Estrutura do projeto

```
├── database.py        # Conexão com o SQLite (engine, SessionLocal, Base, get_db)
├── models.py          # Modelo SQLAlchemy da tabela agendamentos
├── schemas.py         # Schemas Pydantic de entrada e resposta
├── routers/
│   └── agendamentos.py  # Rotas do CRUD
├── main.py            # Instância do FastAPI e create_all()
├── .gitignore
└── README.md
```

## Como instalar

```bash
python -m venv .venv
.venv\Scripts\activate
pip install "fastapi[standard]" sqlalchemy
```

## Como rodar

```bash
fastapi dev main.py
```

Depois abra a documentação interativa (Swagger) em: http://127.0.0.1:8000/docs

## Campos do agendamento

| Campo | Tipo | Descrição |
|---|---|---|
| id | inteiro | Gerado automaticamente |
| cliente | texto | Nome do cliente |
| servico | texto | Serviço (ex: corte, barba) |
| preco | decimal | Valor do serviço |
| horario | texto | Data e hora do agendamento |
| concluido | booleano | Se o atendimento foi concluído |

## Rotas

| Método | Rota | Descrição | Status |
|---|---|---|---|
| POST | /agendamentos/ | Cadastra um novo agendamento | 201 Created |
| GET | /agendamentos/ | Lista todos os agendamentos | 200 OK |
| GET | /agendamentos/?servico=corte | Lista filtrando por serviço | 200 OK |
| PUT | /agendamentos/{id} | Atualiza todos os campos de um agendamento | 200 OK / 404 Not Found |
| DELETE | /agendamentos/{id} | Remove um agendamento | 200 OK / 404 Not Found |

## Exemplo de corpo (POST e PUT)

```json
{
  "cliente": "João",
  "servico": "corte",
  "preco": 35.0,
  "horario": "2026-10-04 15:00",
  "concluido": false
}
```