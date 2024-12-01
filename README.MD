<h1 align="center"> Sistema de Gerenciamento de disciplinas </h1>


![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white) 

Projeto desenvolvido como base para apresentação de um mini-curso sobre FastAPI no Evento SEMITI do IFPB Campus Monteiro


# Funcionalidades do projeto

- `Listagem de todas as disciplinas cadastradas`: o usuário poderá atraves de uma requisição GET no endpoint /disciplinas acessar uma lista contendo todas as disciplinas cadastradas no sistema
- `Cadastrar uma disciplina`: através de uma requisição POST no endpoint /disciplinas o usuário poderá fazer o cadastro de uma disciplina, enviando um JSON contendo o ID, nome e descricao da disciplina.
- `Editar uma disciplina`: Através de uma requisição PUT no endpoint /disciplinas o usuario poderá alterar as informações já salvas de um objeto 
- `Deletar uma disciplina`: Através de uma requisição DELETE no endpoint /disciplinas/{id} o usuario poderá deletar um objeto do sistema, substituindo "{id}" pelo respectivo ID do objeto a ser deletado do sistema  
- `JSON Base`: Caso o endpoint solicite, este será o modelo de JSON a ser enviado
    ```json
    {
        "id" : 32,
        "nome":"Matemática Aplicada a Computação",
        "descricao":"Disciplina voltada a aprimorar os conhecimentos do estudante sobre a matemática dentro do universo da computação"
    }
    ```



# 🛠️ Abrir e rodar o projeto
### você precisa ter o compilador python instalado
Siga o passo-a-passo:
1. abra o GitBash e utilize o comando "git clone  https://github.com/Ygor-Matos/SEMITI" para clonar o projeto.
2. abra o terminal dentro da pasta que foi criada e utilize o comando "pip install -r requirements.txt" e assim o python instalará todas as dependencias do projeto
3. dentro da pasta do projeto, utilize o comando " uvicorn main:app --reload"
4. o uvicorn apresentará uma mensagem como 
    ```
    INFO:     Will watch for changes in these directories: ['xxxx/xxxx/xxxx']
    INFO:     Uvicorn running on http://xxx.x.x.x:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [7655] using StatReload
    INFO:     Started server process [7657]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```
5. copie o link da segunda linha, adicione "/disciplinas" e poderá usar as requisições descritas nas funcionalidades do projeto

# Autor
<a href ="https://github.com/Ygor-Matos">Ygor Silva Matos<a>
