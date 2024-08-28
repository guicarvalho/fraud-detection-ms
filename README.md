# 📊 Detecção de Fraudes em Transações com Cartões de Crédito

Este projeto implementa um sistema de detecção de fraudes em transações com cartões de crédito utilizando **Machine Learning**. A solução inclui um modelo treinado para identificar transações fraudulentas e uma API REST desenvolvida com **FastAPI** para integração e previsão em tempo real.

## 🎯 Objetivo

O objetivo deste projeto é fornecer uma abordagem prática para a detecção de fraudes em transações financeiras, utilizando técnicas de aprendizado de máquina e uma interface de API para facilitar a integração em sistemas maiores.

## 🛠️ Funcionalidades

- **Treinamento do modelo de machine learning:** Utiliza um dataset de transações fictícias para treinar um modelo de regressão logística que detecta fraudes.
- **API REST com FastAPI:** Endpoint `/check-fraud` que recebe dados de transações em JSON e retorna uma resposta indicando se a transação é fraudulenta ou não, junto com a probabilidade associada.
- **Documentação automática:** Integração com Swagger UI para fácil visualização e teste da API.

## 🚀 Tecnologias utilizadas

- **Python:** Linguagem de programação principal.
- **Poetry:** Gerenciador de dependências e ambientes virtuais para Python.
- **Pandas:** Manipulação e análise de dados.
- **scikit-learn:** Biblioteca para construção e avaliação do modelo de machine learning.
- **FastAPI:** Framework para criação de APIs web rápidas e eficientes.
- **Uvicorn:** Servidor ASGI para execução da aplicação FastAPI.
- **Docker:** Plataforma para construir, empacotar e distribuir a aplicação em contêineres.

## 📦 Instalação e execução

1. Clonar o repositório
    ```bash
    git clone https://github.com/guicarvalho/fraud_detection_ms.git
    cd fraud_detection_ms
    ```
2. Escolher a forma de execução
    Você pode optar por executar a aplicação usando Docker ou localmente com Poetry. Ambas as opções estão descritas abaixo:
3. Executando com Docker
    Se você prefere utilizar Docker para executar a aplicação, siga os passos abaixo:
    3.1. Construir a imagem Docker
    ```bash
    docker build -t fraud-detection-ms .
    ```
    3.2. Rodar o contêiner Docker
    ```bash
    docker run -d -p 8000:8000 fraud-detection-ms
    ```
    A aplicação estará acessível em <http://localhost:8000/docs>.

4. Rodando localmente com Poetry
    Caso prefira rodar a aplicação localmente sem Docker, siga os passos abaixo:
    4.1. Instalar o Poetry
    Se ainda não tiver o Poetry instalado, você pode instalá-lo seguindo as instruções oficiais:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    4.2. Instalar as dependências
    No diretório do projeto, execute o comando abaixo para instalar todas as dependências:
    ```bash
    poetry install
    ```
    4.3. Ativar o ambiente virtual
    Ative o ambiente virtual criado pelo Poetry:
    ```bash
    poetry shell
    ```
    4.4. Executar a API FastAPI
    Com o ambiente ativado, execute a aplicação:
    ```bash
    uvicorn src.main:app --reload
    ```
    A aplicação estará acessível em <http://localhost:8000/docs>.

## 🧪 Testando a API

Você pode testar o endpoint `/check-fraud` usando o Swagger UI, Postman, Insomnia ou cURL.

### Exemplo de chamada cURL

```bash
curl -X POST "http://localhost:8000/check-fraud" -H "Content-Type: application/json" -d '{
  "idade": 40,
  "renda_anual": 85000,
  "historico_credito": 0.8,
  "valor": 1200,
  "tipo_transacao": "online",
  "local_transacao": "New York",
  "categoria_comercio": "eletronicos",
  "canal_autenticacao": "online",
  "frequencia_transacoes_24h": 2,
  "distancia_localizacao": 7000,
  "tentativas_falhas_ultimas_24h": 1,
  "hora_transacao": "14:00"
}'
```

### Exemplo de resposta
```json
{
  "result": "legítima",
  "proba": 0.85
}
```

## Contato

Para qualquer dúvida ou sugestão, entre em contato:

- Email: <gui.ifsp11@gmail.com>
- LinkedIn: [Guilherme Carvalho](https://www.linkedin.com/in/decarvalhogui/)
