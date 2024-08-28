# Imagem oficial do Python como base
FROM python:3.11-slim

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando os arquivos de controle de dependências para o diretório de trabalho
COPY pyproject.toml poetry.lock /app/

# Instalando o Poetry
RUN pip install poetry

# Instalando as dependências do projeto ignorando ambiente virtual e dependências de desenvolvimento
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copiando o restante do código da aplicação para o contêiner
COPY . /app

# Expondo a porta 8000 para acesso externo
EXPOSE 8000

# Comando para rodar a aplicação em modo de produção
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" ]
