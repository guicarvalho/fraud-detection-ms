from fastapi import FastAPI

from src.controllers import router

app = FastAPI(
    title="Fraud detection API",
    description="Esta API implementa um sistema de detecção de fraudes em transações com cartões de crédito.",
)
app.include_router(router)
