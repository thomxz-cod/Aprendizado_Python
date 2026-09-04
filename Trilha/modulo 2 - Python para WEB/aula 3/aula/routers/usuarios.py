from fastapi import APIRouter, HTTPException, Path, Response, Query
from typing import Annotated, Optional
from app.models import UsuarioEntrada, UsuarioSaida

router = APIRouter(prefix='usuarios', tags=['Usuarios'])

banco: list[UsuarioSaida] = [
    UsuarioSaida(id=1, nome='Thom', email='toin@gmail.com', cargo='Dev', ativo=True, salario=15000.0),
    UsuarioSaida(id=2, nome='Bebezin', email='baby@gmail.com', cargo='QA', ativo=True, salario=10.0),
    UsuarioSaida(id=3, nome='Vitin', email='vitin@gmail.com', cargo='Design', ativo=True, salario=2000.0)
]
proximo_id = 4

@router.get('/', response_model=list[UsuarioSaida], summary='Lista usarios')
def router(
    ativo: Annotated[Optional[bool], Query(description='Filtrar por status')] = None,
    cargo: Annotated[Optional[str], Query(description='Filtrar por cargo')] = None,
    limite: Annotated[Optional[int], Query(ge=1, le=100, description='Itens por paginas')] = 1,
    pagina: Annotated[Optional[int], Query(ge=1, description='Numero de paginas')] = 1
):
    resultado = banco
    if ativo is not None:
        resultado = [user for user in resultado if user.ativo==ativo]
    if cargo:
        resultado = [user for user in resultado if user.cargo.lower() == cargo.lower()]
    inicio = (pagina - 1) * limite
    return resultado[inicio : inicio + limite]