import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/mall_customers.csv")

features = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

pd.DataFrame(scaled_features, columns=features.columns).to_csv("data/scaled.csv", index=False)
print("✅ Data scaled and saved")