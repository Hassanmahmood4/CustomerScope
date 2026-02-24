import pandas as pd
from pathlib import Path
from sklearn.cluster import KMeans
import joblib

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "scaled.csv"
MODEL_PATH = BASE_DIR / "models" / "kmeans_model.pkl"
OUT_PATH = BASE_DIR / "outputs" / "clustered_customers.csv"

df = pd.read_csv(DATA_PATH)

kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(df)

df_out = df.copy()
df_out["cluster"] = clusters
df_out.to_csv(OUT_PATH, index=False)

joblib.dump(kmeans, MODEL_PATH)

print("✅ Model saved to:", MODEL_PATH)
print("✅ Clustered data saved to:", OUT_PATH)