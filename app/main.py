from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Store em memória. Zera quando o processo reinicia.
_tarefas: dict[int, dict] = {}
_proximo_id = 1


class TarefaIn(BaseModel):
    titulo: str


class TarefaUpdate(BaseModel):
    titulo: str
    concluida: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas", status_code=201)
def criar(tarefa: TarefaIn):
    global _proximo_id
    nova = {"id": _proximo_id, "titulo": tarefa.titulo, "concluida": False}
    _tarefas[_proximo_id] = nova
    _proximo_id += 1
    return nova


@app.get("/tarefas/{tarefa_id}")
def obter(tarefa_id: int):
    if tarefa_id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return _tarefas[tarefa_id]


@app.get("/tarefas")
def listar():
    return list(_tarefas.values())


@app.put("/tarefas/{tarefa_id}")
def atualizar(tarefa_id: int, tarefa: TarefaUpdate):
    if tarefa_id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    _tarefas[tarefa_id]["titulo"] = tarefa.titulo
    _tarefas[tarefa_id]["concluida"] = tarefa.concluida
    return _tarefas[tarefa_id]
