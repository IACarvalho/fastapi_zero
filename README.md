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
