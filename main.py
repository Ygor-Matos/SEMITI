from fastapi import FastAPI, HTTPException
from utils import disciplinaPublic, disciplinaSchema, conversor
from http import HTTPStatus
app= FastAPI()

app.state.disciplinas={}

@app.get("/")
async def getTest():
    return {"message":"teste"}

@app.get("/disciplinas")
async def getDisciplinas():
    return app.state.disciplinas

@app.post("/disciplinas", response_model = disciplinaPublic)
async def postDisciplina(disciplina: disciplinaSchema):
    #salvando a disciplina no banco de dados
    app.state.disciplinas[disciplina.id]=disciplina
    
    #resgatando o objeto do banco de dados
    recuperada= app.state.disciplinas[disciplina.id]
    #recuperando a disciplina salva, mas convertendo-a em uma disciplinaPublic
    disciplinaPublic=conversor(recuperada)

    return disciplinaPublic

@app.delete("/disciplinas/{id}", status_code= HTTPStatus.NO_CONTENT)
async def deleteDisciplina(id: int):
    try:
        app.state.disciplinas.pop(id)
        return
    except:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="disciplina não encontrada")

@app.put("/disciplinas/", response_model=disciplinaPublic)
async def editDisciplina(disciplina: disciplinaSchema):
    if(disciplina.id in app.state.disciplinas):
        app.state.disciplinas[disciplina.id]=disciplina
        recuperada = app.state.disciplinas[disciplina.id]
        disciplinaPublic = conversor(recuperada)
        return recuperada
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail="não há como editar uma cadeira com ID inexistente.")