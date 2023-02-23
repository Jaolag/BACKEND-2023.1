from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Tarefa(BaseModel):
    descricao: str | None
    responsavel:str
    nivel: int 
    situacao: str
    prioridade : int


tarefas: list[Tarefa] = []

for i in range(5):
    Ta = Tarefa(nivel=4+i,
                 responsavel='None',
                 descricao='None',
                 situacao='None',
                 prioridade='0')
    tarefas.append(tarefas)



@app.get('/tarefas')
def todas_tarefas(skip :int | None = None, take: int | None = None):
    inicio = skip

    if skip and take:
        fim = skip + take
    else:
        fim = None
    return tarefas[inicio:fim]

@app.get('/tarefas/{tarefas_situacao}')
def obter_tarefa(tarefas_descricao: int, response: Response):
    for Ta in tarefas:
        if Ta.descricao == tarefas_descricao:
            return Ta

    #naO ACHEI
    #response.status_code = status.HTTP_404_NOT_FOUND
    #return '404 - NOOOOOOOT FOUND!'
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'nao encontrou o Ta descricao = {tarefas_descricao}')

@app.post('/tarefas', status_code=status.HTTP_201_CREATED)                        
def nova_tarefa(Ta: Tarefa):
    tarefas.descricao = len(tarefas) + 100
    tarefas.append(Ta)

    
    return Ta
    
@app.delete("/tarefas/{tarefas_situacao}")
def remover_tarefa(tarefas_descricao: int):
    for tarefa_atual in tarefas:
        if tarefa_atual.descricao == tarefas_descricao:
            tarefas.remove(tarefa_atual)

    raise HTTPException(404, detail="Ta não encontrado")        

@app.put('/tarefas/{tarefas_situacao/descricao}')
def atualizar_tarefa(tarefas_descricao: int, Ta: Tarefa):
    for index in range(len(tarefas)):
        tarefa_atual = tarefas[index]
        if tarefa_atual.descricao == tarefas_descricao:
            tarefas.descricao = tarefa_atual.descricao
            tarefas[index] = Tarefa
            return Tarefa


    raise HTTPException(404,  detail="Ta não encontrado")
