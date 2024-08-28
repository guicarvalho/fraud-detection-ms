from pathlib import Path
from typing import Any

import joblib
import pandas as pd

from src.models import Transaction
from src.utils import hour_to_minutes

BASE_PATH = Path(__file__).parent


class CheckFraudService:
    async def __load_model_and_preprocessor(self) -> tuple[Any, Any]:
        model = joblib.load(f"{BASE_PATH}/ml_model/fraud_detection_model.pkl")
        preprocessor = joblib.load(f"{BASE_PATH}/ml_model/preprocessor.pkl")
        return model, preprocessor

    async def execute(self, transaction: Transaction) -> tuple[str, float]:
        # Carregando o modelo e o pipeline de pré-processamento
        model, preprocessor = await self.__load_model_and_preprocessor()

        # Convertendo a hora para minutos
        transaction_dict = transaction.model_dump()
        transaction_dict["hora_transacao"] = hour_to_minutes(transaction_dict["hora_transacao"])

        # Convertendo para DataFrame e aplicando pré-processamento
        df_transaction = pd.DataFrame([transaction_dict])
        X_transaction = preprocessor.transform(df_transaction)

        # Fazendo a previsão
        prediction = model.predict(X_transaction)[0]
        proba = model.predict_proba(X_transaction)[0][prediction]

        # Interpretando a previsão
        result = "fraudulenta" if prediction == 1 else "legítima"

        return result, proba
