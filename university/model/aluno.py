from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from model import Base, Curso


class Aluno(Base):
    __tablename__ = 'aluno'
    id = Column("pk_id", Integer, nullable=False, primary_key=True)
    cpf = Column(String(14), unique=True, nullable=False)
    nome = Column(String(140), unique=True)
    endereco = Column(String(140))
    cep = Column(String(9))
    cidade = Column(String(30))
    uf = Column(String(2))
    celular = Column(String(14))
    data_matricula = Column(DateTime, default=datetime.now())

    cursos = relationship(Curso, backref="alunos")

    def __init__(self, cpf: str, nome: str, endereco: str, cep: str, cidade: str, uf: str, celular: str, data_matricula: Union[DateTime, None] = None):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
        self.celular = celular
        if data_matricula:
            self.data_matricula = data_matricula

    def adiciona_curso(self, curso: Curso):
        self.cursos.append(curso)
