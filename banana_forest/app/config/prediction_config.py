import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = os.path.join(BASE_DIR, "notebooks", "ml_model.pkl")
DATA_PATH = os.path.join(BASE_DIR, "data", "DataSet2.csv")