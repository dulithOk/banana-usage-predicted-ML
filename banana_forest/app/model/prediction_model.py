from pydantic import BaseModel, Field

class PredictionModel(BaseModel):
    variety_name: str = Field(..., example="Ambul Kesel", description="Name of the banana variety")
    period: str = Field(..., example="January-December", description="Growing period of the variety")
    quantity: int = Field(..., ge=1, example=50, description="Quantity of the bananas (must be positive)")
