from fastapi import FastAPI, Response, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ['http://localhost:5500', 'http://127.0.0.1:5500']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])


class Tarefa(BaseModel):
    id: int | None
    descricao : str
    nivel : int
    prioridade : int
    situacao : str 
    responsavel : str | None

tarefas:list[Tarefa]=[]

#chamar todas as tarefas
@app.get('/tarefas')
def todas_tarefas():
    return tarefas

#pedir tarefa pelo ID
@app.get('/tarefas/{tarefa_id}')
def obter_tarefa(tarefa_id: int, response: Response):
    # print(f'Foi pedido o ID: {tarefa_id}')
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            return tarefa


    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Não existe tarefa com ID: {tarefa_id }')

#postar nova tarefa
@app.post('/tarefas', status_code=status.HTTP_201_CREATED)
def nova_tarefa(tarefa: Tarefa):
    tarefa.id = len(tarefas) + 1
    tarefas.append(tarefa)

    return tarefa

#atualizar tarefa pelo ID
@app.put('/tarefas/{tarefa_id}')
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa):
    for index in range(len(tarefas)):
        tarefa_atual = tarefas[index]
        if tarefa_atual.id == tarefa_id:
            tarefa.id = tarefa_atual.id
            tarefas[index] = tarefa
            return tarefa

    raise HTTPException(status.HTTP_404_NOT_FOUND,
                        detail="Tarefa nao existe")

#remover tarefa pelo ID
@app.delete("/tarefas/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def apagar_tarefa(tarefa_id: int):
    for tarefa_atual in tarefas:
        if tarefa_atual.id == tarefa_id:
            tarefas.remove(tarefa_atual)
            return

    raise HTTPException(status.HTTP_404_NOT_FOUND,
                        detail="Essa tarefa nao existe")
