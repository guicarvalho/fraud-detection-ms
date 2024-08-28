from pydantic import BaseModel


# Definindo o modelo de dados esperado para a transação
class Transaction(BaseModel):
    idade: int
    renda_anual: float
    historico_credito: float
    valor: float
    tipo_transacao: str
    local_transacao: str
    categoria_comercio: str
    canal_autenticacao: str
    frequencia_transacoes_24h: int
    distancia_localizacao: float
    tentativas_falhas_ultimas_24h: int
    hora_transacao: str
