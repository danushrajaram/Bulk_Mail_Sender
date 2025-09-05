# data_loader.py
import pandas as pd
from config import CSV_FILE

def load_participants():
    df = pd.read_csv(CSV_FILE, dtype=str)  # force all to strings
    df = df.fillna("")  # replace NaN with empty string
    return df.to_dict(orient="records")
