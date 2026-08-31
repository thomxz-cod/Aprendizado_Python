from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, field_validator
from typing import Optional



app = FastAPI(
    title="Primeria API do Thomxz :P",
    description="Primeira API com FastAPI",
    version="0.2.1"
)

@app.get("/")
def raiz():
    return RedirectResponse(url="/docs")

@app.get("/status") # status dos serviços
def status():
    return {"API": {"status":"active", "version":"0.2.1", "msg":"API Rodando fi :/"}}


class Usuario(BaseModel):
    nome: str
    email: str
    cargo: str
    ativo: bool = True
    salario: Optional[float] = None

    @field_validator('nome')
    @classmethod
    def validar_nome(cls, v):
        v = v.strip()
        if len(v) < 3:
            raise ValueError('Nome deve ter pelo menos 3 caracteres!')
        return v.title()

    @field_validator('salario')
    @classmethod
    def validar_nome(cls, v):
        if v is None:
            return v
        if v <= 0:
            raise ValueError("O salario nao pode ser menor ou igual a 0")
        return v

class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str
    ativo: bool = True
    salario: Optional[float] = None

users_db: list[UsuarioResposta] = [
    UsuarioResposta(id=1, nome='Thom', email='toin@gmail.com', cargo='Pentest in CyberSecurity', ativo=True, salario=15000.0),
    UsuarioResposta(id=2, nome='Bebezin', email='baby@gmail.com', cargo='Dev', ativo=True, salario=10.0),
    UsuarioResposta(id=3, nome='Vitin', email='vitin@gmail.com', cargo='Devinho', ativo=True, salario=2000.0)
]
next_id = 4

@app.get("/users")
def list_users():
    return users_db

@app.get("/users/search_user_id/{id}", response_model=UsuarioResposta)
def list_user_id(id: int):
    for user in users_db:
        if  user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User não encontrado! T-T")

@app.post('/users', response_model=UsuarioResposta, status_code=201)
def create_user(data: Usuario):
    global next_id
    for user in users_db:
        if user.email == data.email:
            raise HTTPException(400, 'E-mail já cadastrado')
    new = UsuarioResposta(id=next_id, **data.model_dump())
    users_db.append(new)
    next_id += 1
    return new

@app.put('/users/{id}', response_model=UsuarioResposta)
def update_user(id: int, data:Usuario):
    for i, user in enumerate(users_db):
        if user.id == id:
            update = UsuarioResposta(id=id, **data.model_dump())
            users_db[i] = update
            return update
    raise HTTPException(status_code=404, detail="User não encontrado! T-T")

@app.delete('/users/{id}', status_code=204)
def delete_user(id: int):
    for u in users_db:
        if u.id == id:
            users_db.remove(u)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="User não encontrado! T-T")

