# Projeto criado no curso fastapi do zero do canal Dunosauro

## Criaçāo do Projeto
```shell
# Usando a flag --flat faz com sem a pasta src
poetry new --flat fastapi_zero
```

## Instalando versões alternativas do python com poetry
```shell
poetry python install 3.13 #instala a versões 13.3 do python
poetry python list # Lista as versões python instaladas
```
## definindo a versão do python a ser usada

```shell
poetry env use 3.13
```
## instalação dos pacotes usando poetry
```shell
poetry add "fastapi[standard]"
```

## Executando o Projeto
```shell
# Executando sem ambiente virtual
poetry run fastapi dev fastapi_zero/app.py
#Entrando no ambiente virtual
poetry shell
#Executa o projeto em modo de desenvolvimento
fastapi dev fastapi_zero/app.py
```
### Acessando o projeto
- http://localhost:8000 -> Acessa a rota raiz
- http://localhost:8000/docs -> Acessa a documentação da API via swagger
- http://localhost:8000/redoc -> Acessa a documentação Redoc, uma documentação mais detalhada


## Testes em três etapas (AAA)
- A : Arrange -> Arranjo
- A : Act -> Execute a coisa (o SUT)
- A : Assert -> Verifica se o resultado é o esperado

```python
from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retorna_ola_mundo():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Hello World'}
```

## Criando gitignore com pipx

```shell
pipx run ignr -p python > .gitignore
```

## Usando a CLI do github
```shell
# faça login no github
gh auth login
# Crie um repositório
gh repo create
```

## Pydantic
Bliblioteca para validação, e ajuda na camada de documentação da API. Ele cria um schema (contrato) de validação para os dados de entrada e saída da API.

## SQLalchemy
É uma espécie de ORM, mas é muito mais poderoso do que um simples ORM.


## Criadno migrations
Instale a biblioteca alembic
inicie o alembic
```shell
alembic init migrations
```
configure *env.py* criado na pasta migraitons
```py
# direciona para a configuraçāo do database
config.set_main_option('sqlalchemy.url', Settings().DATABASE_URL)
# direciona para as classes representantes das tabelas
target_metadata = table_registry.metadata
```
execute o comando para gerar uma migration
```shell
alembic revision --autogenerate -m "create user table"
```
--autogenerate -> busca nos metadatas e faz as configurações
-m -> passa uma mensagem descrevendo o que está sendo feito

executando a migration:
```shell
alembic upgrade head
```

para retornar uma versāo:
```shell
alembic downgrade -1
# o -1 sigfica que queremos voltar uma versão
```

## vizualizando o database sqlite usadno o halerquin
basta rodar o seguinte comando:
```shell
pipx run harlequin database.db
```
