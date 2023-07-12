from pydantic import BaseModel


class CursoSchema(BaseModel):
    id: int = 1
    cpf: str = "123.332.434-20"
    codigo_curso: int = "16142584"
    curso: str = "Psicologia"
    codigo_disc: int = "22143456"
    disciplina: str = "Psicologia Hospitalar"
    creditos: int = 8
