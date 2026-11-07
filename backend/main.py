
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import os

# Conexão com PostgreSQL
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


# MODELOS
class Usuario(BaseModel):
    nome: str
    email: str
    senha: str


class Login(BaseModel):
    email: str
    senha: str


class Chamado(BaseModel):
    titulo: str
    descricao: str
    categoria: str
    prioridade: str


class AtualizarStatus(BaseModel):
    status: str


# CADASTRO DE USUÁRIO
@app.post("/usuarios")
def cadastrar_usuario(usuario: Usuario):
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO usuarios (nome, email, senha)
        VALUES (%s, %s, %s)
        """,
        (usuario.nome, usuario.email, usuario.senha)
    )

    conexao.commit()
    cursor.close()

    return {
        "mensagem": "Usuário recebido com sucesso",
        "nome": usuario.nome,
        "email": usuario.email
    }


# LOGIN
@app.post("/login")
def fazer_login(login: Login):
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT * FROM usuarios
        WHERE email = %s AND senha = %s
        """,
        (login.email, login.senha)
    )

    usuario_encontrado = cursor.fetchone()
    cursor.close()

    if usuario_encontrado:
        return {
            "mensagem": "login realizado com sucesso",
            "tipo": usuario_encontrado[4]
        }

    return {"mensagem": "E-mail ou senha incorretos"}


# ABERTURA DE CHAMADOS
@app.post("/chamados")
def abrir_chamado(chamado: Chamado):
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO chamados
        (titulo, descricao, categoria, prioridade)
        VALUES (%s, %s, %s, %s)
        """,
        (
            chamado.titulo,
            chamado.descricao,
            chamado.categoria,
            chamado.prioridade
        )
    )

    conexao.commit()
    cursor.close()

    return {"mensagem": "Chamado recebido com sucesso"}


# LISTAR CHAMADOS
@app.get("/chamados")
def listar_chamados():
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM chamados ORDER BY id")

    chamados = cursor.fetchall()
    cursor.close()

    return {"chamados": chamados}


# ATUALIZAR STATUS E REGISTRAR HISTÓRICO - AC3
@app.put("/chamados/{chamado_id}/status")
def atualizar_status(chamado_id: int, dados: AtualizarStatus):
    cursor = conexao.cursor()

    try:
        # Consulta o status anterior
        cursor.execute(
            "SELECT status FROM chamados WHERE id = %s FOR UPDATE",
            (chamado_id,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            conexao.rollback()
            return {"mensagem": "Chamado não encontrado"}

        status_anterior = resultado[0]

        # Atualiza o status do chamado
        cursor.execute(
            """
            UPDATE chamados
            SET status = %s
            WHERE id = %s
            """,
            (dados.status, chamado_id)
        )

        # Registra somente quando o status muda
        if status_anterior != dados.status:
            cursor.execute(
                """
                INSERT INTO historico_chamados
                (chamado_id, status_anterior, status_novo)
                VALUES (%s, %s, %s)
                """,
                (
                    chamado_id,
                    status_anterior,
                    dados.status
                )
            )

        conexao.commit()

        return {"mensagem": "Status atualizado com sucesso"}

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()


# ASSUMIR CHAMADO - AC3
@app.put("/chamados/{chamado_id}/assumir")
def assumir_chamado(chamado_id: int):
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            UPDATE chamados
            SET tecnico_responsavel = 6
            WHERE id = %s
              AND tecnico_responsavel IS NULL
            RETURNING id
            """,
            (chamado_id,)
        )

        atualizado = cursor.fetchone()
        conexao.commit()

        if atualizado is None:
            return {
                "mensagem": "Chamado inexistente ou já atribuído"
            }

        return {"mensagem": "Chamado assumido com sucesso"}

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()


# CONSULTAR HISTÓRICO DE UM CHAMADO - AC3
@app.get("/chamados/{chamado_id}/historico")
def consultar_historico(chamado_id: int):
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT id, chamado_id, status_anterior,
               status_novo, data_alteracao
        FROM historico_chamados
        WHERE chamado_id = %s
        ORDER BY data_alteracao, id
        """,
        (chamado_id,)
    )

    historico = cursor.fetchall()
    cursor.close()

    return {"historico": historico}
