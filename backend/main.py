from sqlite3 import Cursor

from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import psycopg2 
import os

conexao = psycopg2.connect(
    host="localhost",
    database="helpdesk_ti",
    user="postgres",
    password=os.getenv("DB_PASSWORD")
)
conexao.set_client_encoding("UTF8")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Usuario(BaseModel):
    nome: str
    email: str
    senha: str
class Login(BaseModel):
    email: str
    senha: str


@app.post("/usuarios")
def cadastrar_usuario(usuario: Usuario):
    cursor = conexao.cursor()

    cursor.execute(
    "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
    (usuario.nome, usuario.email, usuario.senha)
)
    conexao.commit()

    return {
        "mensagem": "Usuário recebido com sucesso",
        "nome": usuario.nome,
        "email": usuario.email
    }
@app.post("/login")
def fazer_login(login: Login):
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT * FROM usuarios WHERE email = %s AND senha = %s",
            (login.email, login.senha)
   )
    usuario_encontrado = cursor.fetchone()
    if usuario_encontrado:
        return {"mensagem": "login realizado com sucesso"}
    
    return {"mensagem": "E-email ou senha incorretos"}
class Chamado(BaseModel):
    titulo: str
    descricao: str
    categoria: str
    prioridade: str

@app.post("/chamados")
def abrir_chamado(chamado: Chamado):
    cursor = conexao.cursor()

    cursor.execute(
    "INSERT INTO chamados (titulo, descricao, categoria, prioridade) VALUES (%s, %s, %s, %s)",
    (chamado.titulo, chamado.descricao, chamado.categoria, chamado.prioridade)
)
    conexao.commit()

    return {"mensagem": "Chamado recebido com sucesso"}
@app.get("/chamados")
def listar_chamados():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM chamados")
    chamados = cursor.fetchall()

    return{"chamados": chamados}
    