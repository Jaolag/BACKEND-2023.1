from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Tarefa(BaseModel):
    descricao : str
    responsavel : str | None
    nivel : int
    situacao : str | None
    prioridade : int
    
tarefas: list[Tarefa]=[]

@app.get('/tarefa')
def todas_tarefas():
    return tarefas

@app.post('/tarefa/{adicionar}')                        
def nova_tarefa(tarefa: Tarefa):
    tarefa.situacao = len(tarefas) +100
    tarefas.append(tarefa)

    
    return tarefa

'''--!--Delete Em Fase de Beta--!--

@app.delete('/tarefa/{situacao}')
def remove_tarefa(situacao: int):
    for tarefa_atual in tarefas:
        if tarefa_atual.situacao == situacao:
            tarefas.remove(tarefa_atual)

    raise HTTPException(404, detail="Tarefa não existe")  '''
