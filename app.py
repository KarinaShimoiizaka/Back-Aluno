from Aluno import Aluno
from fastapi import FastAPI, Query
from typing import Annotated
from datetime import date

app = FastAPI()

aluno = Aluno()

@app.post("/aluno/insert")
def aluno_insert(
    nome: str, 
    sobrenome : str, 
    nascimento : date, 
    media: Annotated[float, Query(ge=0, le=10)],
    academia : int, 
    data_mat: date, 
    ):
    result = aluno.insert(nome,sobrenome,nascimento,media,academia,data_mat)
    print(result)
    return result

@app.get("/aluno/select")
def aluno_select(
    mat: int
    ):
    result = aluno.select(mat)
    return result

@app.update("/aluno/update")
def aluno_update(
    mat : int,
    media: Annotated[float, Query(ge=0, le=10)],    
    ):
    result = aluno.update(media,mat)
    return result

@app.delete("/aluno/delete")
def aluno_delete(
    mat: int
    ):
    result = aluno.delete(mat)
    return result