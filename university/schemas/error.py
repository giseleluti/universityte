from pydantic import BaseModel


class ErrorViewSchema(BaseModel):
    mensagem: str
