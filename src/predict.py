import joblib
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "kmeans_model.pkl"

kmeans = joblib.load(MODEL_PATH)

def predict_segment(income, spending):
    scaler = StandardScaler()
    X = [[income, spending]]
    X_scaled = scaler.fit_transform(X)
    cluster = kmeans.predict(X_scaled)[0]
    return cluster

if __name__ == "__main__":
    income = float(input("Enter annual income (k$): "))
    spending = float(input("Enter spending score (1-100): "))

    cluster = predict_segment(income, spending)
    print(f"🧠 Customer belongs to cluster: {cluster}")