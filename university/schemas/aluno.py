from pydantic import BaseModel
from typing import List
from model.aluno import Aluno

from schemas.curso import CursoSchema


class AlunoSchema(BaseModel):
    cpf: str = "123.332.434-20"
    nome: str = "Luciana da Silva Santos"
    endereco: str = "Estrada Botucatu, 1059, Campo Grande"
    cidade: str = "Volta Redonda"
    uf: str = "RJ"
    cep: str = "23664-023"
    celular: str = "(22) 91932-1455"


class AlunoGetSchema(BaseModel):
    cpf: str = "123.332.434-20"
    nome: str = "Luciana da Silva Santos"

class ListagemAlunoSchema(BaseModel):
    alunos: List[AlunoSchema]


def view_alunos(alunos: List[Aluno]):
    resultado = []
    for aluno in alunos:
        resultado.append({
            "cpf": aluno.cpf,
            "nome": aluno.nome,
            "endereco": aluno.endereco,
            "cep": aluno.cep,
            "cidade": aluno.cidade,
            "uf": aluno.uf,
            "celular": aluno.celular,
        })

    return {"alunos": resultado}


class AlunoViewSchema(BaseModel):
    id: int = 1
    cpf: str = "123.332.434-20"
    nome: str = "Luciana da Silva Santos"
    endereco: str = "Estrada Botucatu, 1059, Campo Grande"
    cidade: str = "Volta Redonda"
    uf: str = "RJ"
    cep: str = "23664-023"
    celular: str = "(22) 91932-1455"
    cursos: List[CursoSchema]


class AlunoDelSchema(BaseModel):
    mensagem: str
    cpf: str


def view_aluno(aluno: Aluno):
    return {
        "id": aluno.id,
        "cpf": aluno.cpf,
        "nome": aluno.nome,
        "endereco": aluno.endereco,
        "cep": aluno.cep,
        "cidade": aluno.cidade,
        "uf": aluno.uf,
        "celular": aluno.celular,
        "total_cursos": len(aluno.cursos),
        "cursos": [{"curso": c.curso, "disciplina": c.disciplina, "creditos": c.creditos} for c in aluno.cursos]
    }
