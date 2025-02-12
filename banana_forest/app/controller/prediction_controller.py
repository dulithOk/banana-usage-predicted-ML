from fastapi import APIRouter, Response
from app.model.prediction_model import PredictionModel
from app.service.prediction_service import PredictionService

router = APIRouter(
    prefix="/v1/banana",
    tags=["Banana Prediction"]
)
prediction_service = PredictionService()

@router.post("/get")
async def crawler_cron(response: Response, prediction_model: PredictionModel):
    res_data, status_code = prediction_service.predict_best_use(prediction_model=prediction_model)
    response.status_code = status_code
    return res_data

