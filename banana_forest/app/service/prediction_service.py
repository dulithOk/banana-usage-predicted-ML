from app.core.ml_core import MLModel
from app.model.prediction_model import PredictionModel
from app.model.generic_response import GenericResponse

class PredictionService:
    def __init__(self):
        # Initialize the ML model
        self.ml_model = MLModel()

    def predict_best_use(self, prediction_model: PredictionModel):
        """
        Predicts the best use of a given banana variety based on input parameters.

        Args:
            prediction_model (PredictionModel): An instance containing the variety name, 
                                                period (month), and quantity.

        Returns:
            tuple: A tuple containing a GenericResponse object and an HTTP status code.
                   - Success: (GenericResponse, 200) with predicted use and confidence score.
                   - Failure: (GenericResponse, 500) with an error message.
        """
        try:
            result, confidence = self.ml_model.predict(
                variety_name=prediction_model.variety_name,
                period=prediction_model.period,
                quantity=prediction_model.quantity
            )
            
            return GenericResponse.success(message="ML Model Process Success",
                                           results={
                                               "predicted_use": result,
                                               "confidence_score": confidence
                                               }), 200
        except Exception as e:
            return GenericResponse.failed(message=f"ML Model Process Failed Error: {e}",
                                          results=None), 500    
            
