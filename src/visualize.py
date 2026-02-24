import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Resolve project root
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "outputs" / "clustered_customers.csv"

# Load clustered data
df = pd.read_csv(DATA_PATH)

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

# Detect column names dynamically
if "income_scaled" in df.columns and "spending_scaled" in df.columns:
    x_col = "income_scaled"
    y_col = "spending_scaled"
    x_label = "Income (scaled)"
    y_label = "Spending Score (scaled)"
elif "Annual Income (k$)" in df.columns and "Spending Score (1-100)" in df.columns:
    x_col = "Annual Income (k$)"
    y_col = "Spending Score (1-100)"
    x_label = "Annual Income (k$)"
    y_label = "Spending Score (1–100)"
else:
    raise ValueError(f"❌ Could not find suitable columns to plot. Found: {df.columns.tolist()}")

# Plot clusters
plt.figure(figsize=(8, 6))
plt.scatter(
    df[x_col],
    df[y_col],
    c=df["cluster"],
    cmap="viridis",
    s=40,
    alpha=0.85,
)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title("Customer Segmentation (K-Means Clusters)")
plt.colorbar(label="Cluster")
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()