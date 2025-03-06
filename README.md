# Back Aluno

## Introdução

O projeto **Back Aluno** é uma API que implementa um CRUD (Create, Read, Update, Delete) básico para gerenciar informações de alunos. Ele permite realizar operações como inserir, deletar, atualizar e buscar registros de forma eficiente, proporcionando um ambiente ideal para o desenvolvimento de habilidades em manipulação de banco de dados e construção de APIs RESTful.

O sistema gerencia dados essenciais sobre os alunos, incluindo:
- **Matrícula (ID)**: Identificador único do aluno.
- **Nome** e **Sobrenome**: Informações pessoais para identificação.
- **Data de Nascimento**: Para cálculo de idade e validações.
- **Média do Aluno**: Indicador de desempenho acadêmico.
- **Academia**: Associação à instituição de ensino.
- **Data de Matrícula**: Registro da data de entrada na academia.

Esse projeto não só auxilia no aprendizado sobre a estrutura de um CRUD, como também prepara o usuário para lidar com desafios reais de desenvolvimento backend, utilizando tecnologias modernas como **FastAPI** e **PostgreSQL**.

## Índice

- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Requisitos e Dependências](#requisitos-e-dependências)
- [Instalação](#instalação)
- [Execução](#execução)
- [Exemplo de Uso](#exemplo-de-uso)
- [Contribuidores](#contribuidores)


---

## Funcionalidades



## Tecnologias

O projeto foi realizado utilizando as seguintes tecnologias e linguagens:

- **Python**: Linguagem de programação principal do projeto.
- **FastAPI**: Framework para construção de APIs.
- **PostgreSQL**: Banco de dados relacional.
- 

## Requisitos e Dependências

Para executar este projeto de CRUD utilizando FastAPI e PostgreSQL, os seguintes requisitos e dependências devem ser atendidos:

### Requisitos Mínimos

1. **Sistema Operacional**:
   - Windows 10 ou superior
   - macOS Monterey ou superior
   - Distribuições Linux compatíveis com Docker

2. **Software Necessário**:
   - [Python 3.10+](https://www.python.org/downloads/)
   - [Docker](https://www.docker.com/get-started)
   - [Docker Compose](https://docs.docker.com/compose/install/)
   - [PgAdmin 4](https://www.pgadmin.org/download/)

### Dependências do Projeto

O projeto utiliza as seguintes bibliotecas e frameworks, que devem ser instalados no ambiente virtual do Python:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` contém:

```
fastapi==0.95.1
uvicorn==0.21.1
psycopg2==2.9.6
dotenv==0.21.1
```

### Configuração do Banco de Dados

O banco de dados PostgreSQL é gerenciado através de um container no Docker. Para garantir sua configuração adequada:

1. Certifique-se de que o Docker está instalado e em execução.
2. No diretório do projeto, crie um arquivo `.env` contendo a string de conexão com o banco de dados:
   ```
   DATABASE_URL=postgresql://usuario:senha@localhost:5432/dbGerminare
   ```
3. Execute o seguinte comando para subir o container:
   ```bash
   docker-compose up -d
   ```
4. Acesse o PgAdmin e conecte-se ao banco de dados `dbGerminare`.
5. Certifique-se de que a tabela `aluno` está criada com as seguintes colunas:
   ```sql
   CREATE TABLE aluno (
       mat SERIAL PRIMARY KEY,
       nome VARCHAR(50) NOT NULL,
       sobrenome VARCHAR(50) NOT NULL,
       nascimento DATE NOT NULL,
       media FLOAT CHECK (media BETWEEN 0 AND 10),
       academia INT NOT NULL,
       data_mat DATE NOT NULL
   );
   ```



## Instalação

Instale as dependências com o pip e certifique-se de ter o Python instalado em sua máquina. Criar um ambiente virtual é opcional, mas recomendado.

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Execução

Para iniciar o servidor, certifique-se de que seu ambiente virtual está ativado, caso esteja utilizando um.

```bash
fastapi dev app.py
```

## Exemplo de Uso

Para começar a fazer requisições à sua API, você pode usar o Postman, um navegador ou qualquer outro framework de sua preferência. Basta colar a URL da API e o caminho desejado para testá-la.

```bash
http://127.0.0.1:8000/select
```


## Contribuidores

<table>
  <tr>
    <td align="center"><a href=""><img style="border-radius: 50%;" src="https://media-gru2-2.cdn.whatsapp.net/v/t61.24694-24/454843579_1145731036495440_3954503991619474896_n.jpg?ccb=11-4&oh=01_Q5AaIFdEAL9hMY22iyMSF79SU_1Jm628t6zws4yL9mF6GpI1&oe=67CB8678&_nc_sid=5e03e0&_nc_cat=108" width="100px;" alt=""/><br /><sub><b>Giovanna da Rosa</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat"></a></td>
    <td align="center"><a href=""><img style="border-radius: 50%;" src="https://media-gru2-2.cdn.whatsapp.net/v/t61.24694-24/473400583_570136939220948_4871412455034400056_n.jpg?ccb=11-4&oh=01_Q5AaIFiUSX4OyThlrSEAOkxf8EdAibtbitW0Z9NzpFEb4YSh&oe=67CBA34C&_nc_sid=5e03e0&_nc_cat=104" width="100px;" alt=""/><br /><sub><b>Mayumi Castiglioni</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat"></a></td>
    <td align="center"><a href=""><img style="border-radius: 50%;" src="https://media-gru2-2.cdn.whatsapp.net/v/t61.24694-24/473402743_674316331821967_6392751150344836676_n.jpg?ccb=11-4&oh=01_Q5AaIJykY2yE9zU7RF1pFUrTBfCj2sviIleAqYzPqxVKUMDK&oe=67CB9E5F&_nc_sid=5e03e0&_nc_cat=104" width="100px;" alt=""/><br /><sub><b>Karina Shimoiizaka</b></sub></a><br /><a href="" title="Rocketseat"></a></td>
    <td align="center"><a href=""><img style="border-radius: 50%;" src="https://media-gru2-2.cdn.whatsapp.net/v/t61.24694-24/465207516_27670201709293748_1423815965972246024_n.jpg?ccb=11-4&oh=01_Q5AaIJluJR-GSpa7qX5ZG7mluiHzxw5hjw7eF5hHUP1CjdJU&oe=67CB81CE&_nc_sid=5e03e0&_nc_cat=106" width="100px;" alt=""/><br /><sub><b>Letícia Nascimento</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat"></a></td>
  </tr>
</table>

