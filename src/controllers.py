from fastapi import APIRouter

router = APIRouter()


@router.get("/check-fraud")
async def check_fraud():
    return {"result": "legítima", "accuracy": 0.85}
