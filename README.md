# Exercício 4.1 — API REST de uma aplicação de TODO list (POST/GET/PUT)

**Aluno:** Elisangela Andrade Rocha Osorio
**Disciplina:** IDP-TD 2026
**Framework usado:** FastAPI + Uvicorn_

---

## O que esta API faz

API REST que serve de **backend de uma aplicação de TODO list** — gerencia
**tarefas** (`{id, titulo, concluida}`), com armazenamento em memória, rodando em
`http://localhost:8000`. Implementa POST (criar), GET (ler) e
PUT (atualizar), seguindo o contrato do [tutorial_4.1.md](tutorial_4.1.md#3-contrato-da-api-obrigatório--o-autograder-depende-disto).

## Estrutura

- [app/main.py](app/main.py) — implementação da API
- [requirements.txt](requirements.txt) — dependências (`fastapi`, `uvicorn`)
- [`.autograde-exercise`](.autograde-exercise) — marcador do autograder (conteúdo: `4.1`)

## Como rodar

```bash
pip install -r requirements.txt
uvicorn app.main:app --port 8000
```

## Como validar

Com a API rodando (recém-reiniciada, store vazio), em outro terminal dentro do repo:

```bash
autograde validar 4.1
```

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/health` | liveness — `{"status":"ok"}` |
| POST | `/tarefas` | cria tarefa a partir de `{"titulo": "..."}` |
| GET | `/tarefas/{id}` | lê uma tarefa (404 se não existe) |
| GET | `/tarefas` | lista todas |
| PUT | `/tarefas/{id}` | atualiza `titulo` e `concluida` |

## Decisões de implementação

**Por que FastAPI?** Escolhi o FastAPI porque ele facilita bastante a criação de APIs em Python. Ele já se responsabiliza por validar os dados que chegam nas requisições e gera uma documentação automática que ajuda a testar os endpoints pelo navegador.

**Como as tarefas são guardadas?** As tarefas ficam salvas em um dicionário Python na memória. Cada tarefa recebe um ID numérico que vai aumentando (1, 2, 3...). Como o exercício pede, tudo zera quando a API é reiniciada — não tem banco de dados, e isso é proposital para o autograder funcionar com estado limpo.

**Como separei os dados de entrada?** Criei dois modelos: um para criação (que recebe só o `titulo`) e outro para atualização (que recebe `titulo` e `concluida`). Assim cada endpoint aceita só o que precisa.

**E quando a tarefa não existe?** Nos endpoints de buscar e atualizar uma tarefa por ID, se o ID não existir no dicionário, a API retorna erro 404 com a mensagem "Tarefa não encontrada", como o contrato do exercício pede.
