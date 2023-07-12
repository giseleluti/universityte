from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from sqlalchemy.orm import relationship

from model import Base


class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, nullable=False, primary_key=True)
    cpf = Column(String(14), nullable=False)
    codigo_curso = Column(Integer)
    curso = Column(String(100))
    codigo_disc = Column(Integer)
    disciplina = Column(String(80))
    creditos = Column(Integer)
    data_matricula = Column(DateTime, default=datetime.now())

    aluno_id = Column(Integer, ForeignKey("aluno.pk_id"), nullable=False)
    aluno = relationship("Aluno")

    def __init__(self, cpf: str, codigo_curso: int, curso: str, codigo_disc: int, disciplina: str, creditos: int, data_matricula: Union[DateTime, None] = None):
        self.cpf = cpf
        self.codigo_curso = codigo_curso
        self.curso = curso
        self.codigo_disc = codigo_disc
        self.disciplina = disciplina
        self.creditos = creditos

        if data_matricula:
            self.data_matricula = data_matricula
