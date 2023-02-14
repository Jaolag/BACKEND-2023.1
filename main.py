from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Filme(BaseModel):
    id: int | None
    nome:str
    genero: str
    ano: int
    duracao : int


filmes: list[Filme] = []

for i in range(10):
    filme = Filme(id=100+i,
                 nome='Titanic',
                 genero='Romance',
                 ano=1997,
                 duracao=150)
    filmes.append(filme)



@app.get('/filmes')
def todos_filmes(skip :int | None = None, take: int | None = None):
    inicio = skip

    if skip and take:
        fim = skip + take
    else:
        fim = None
    return filmes[inicio:fim]

@app.get('/filmes/{filme_id}')
def obter_filme(filme_id: int, response: Response):
    for filme in filmes:
        if filme.id == filme_id:
            return filme

    #naO ACHEI
    #response.status_code = status.HTTP_404_NOT_FOUND
    #return '404 - NOOOOOOOT FOUND!'
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'nao encontrou o filme id = {filme_id}')

@app.post('/filmes', status_code=status.HTTP_201_CREATED)                        
def novo_filme(filme: Filme):
    filmes.id = len(filmes) + 100
    filmes.append(filme)

    
    return filme
    
