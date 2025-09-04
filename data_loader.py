# data_loader.py
import pandas as pd
from config import CSV_FILE

def load_participants():
    """Load participant data from CSV into list of dicts"""
    df = pd.read_csv(CSV_FILE)
    participants = df.to_dict(orient="records")
    return participants
