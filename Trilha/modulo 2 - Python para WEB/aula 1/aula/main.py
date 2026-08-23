from fastapi import FastAPI     # importa a função de criação de API
from fastapi.responses import RedirectResponse # importa redirecionador do fastAPI
import json                     # importa a biblioteca nativa do python para manipular arquivos .json 


with open("users_db.json", "r", encoding="utf-8") as file:
    users_db = json.load(file)
"""
abre o .json em forma de leitura(r = read) e coloca em um dicionario python
encoding="utf-8"                # garante que ate caracteres especiais serão lidos
users_db = json.load(file)      # converte a data do arquivo .json prum dicionario in python
"""



app = FastAPI(
    title="Primeria API do Thomxz :P",
    description="Primeira API com FastAPI",
    version="0.1.0"
)

@app.get("/")       # pra quando alguem entrar na pasta raiz ser redirecionado pra /docs
def raiz():
    return RedirectResponse(url="/docs")

@app.get("/status") # status dos serviços
def status():
    return {"API": {"status":"active", "version":"0.1.0", "msg":"API Rodando fi :/"}}

@app.get("/users")  # retorna toda a lista de usuarios
def list_users():
    return users_db

@app.get("/users/search_user_name/{user_name}")
def list_user_name(name: str = ''):
    if not name:
        return users_db
    return [user for user in users_db if name.lower() in user['name'].lower()]

@app.get("/users/search_user_id/{user_id}")    # retorna o usuario com o ID que o cliente passou, utilize chaves{} para parametros
def list_user_id(id: int):      # id: int diz que a variavel id é um numero inteiro
    for user in users_db:
        if id == user["id"]:
            return user
    return {"Error":"User não encontrado! T-T"}

