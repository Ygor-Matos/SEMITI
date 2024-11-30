from pydantic import BaseModel
from typing import Optional
from typing import Optional


class disciplinaSchema(BaseModel):
    id: int
    nome: str
    descricao: str

class disciplinaPublic(BaseModel):
    nome: str
    descricao: str

def conversor(disciplina :disciplinaSchema) -> disciplinaPublic:
    return disciplinaPublic(nome=disciplina.nome, descricao=disciplina.descricao)