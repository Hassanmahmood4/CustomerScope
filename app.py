import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="CustomerScope – Customer Segmentation Dashboard",
    layout="wide"
)

st.title("🧠 CustomerScope – Customer Segmentation Dashboard")
st.markdown("Analyze customer clusters generated using K-Means.")

DATA_PATH = "outputs/clustered_customers.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

# Load data
try:
    df = load_data()
except FileNotFoundError:
    st.error("❌ Clustered data not found. Please run train.py first.")
    st.stop()

# Sidebar filters
st.sidebar.header("🔍 Filters")
clusters = sorted(df["cluster"].unique().tolist())

selected_clusters = st.sidebar.multiselect(
    "Select clusters to display",
    options=clusters,
    default=clusters
)

filtered_df = df[df["cluster"].isin(selected_clusters)]

# KPIs
st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", len(filtered_df))

with col2:
    st.metric("Number of Clusters", filtered_df["cluster"].nunique())

with col3:
    st.metric("Total Customers", len(filtered_df))
    st.metric("Clusters Selected", len(selected_clusters))

# Cluster distribution (Matplotlib bar chart)
st.subheader("📊 Cluster Distribution")

counts = filtered_df["cluster"].value_counts().sort_index()

fig1, ax1 = plt.subplots()
ax1.bar(counts.index.astype(str), counts.values)
ax1.set_xlabel("Cluster")
ax1.set_ylabel("Count")
ax1.set_title("Customers per Cluster")

st.pyplot(fig1)

# Scatter plot (Matplotlib)
st.subheader("🧬 Customer Clusters (Income vs Spending Score)")

fig2, ax2 = plt.subplots()

for c in clusters:
    cluster_data = filtered_df[filtered_df["cluster"] == c]
    ax2.scatter(
        cluster_data["Annual Income (k$)"],
        cluster_data["Spending Score (1-100)"],
        label=f"Cluster {c}",
        alpha=0.7
    )

ax2.set_xlabel("Annual Income (k$)")
ax2.set_ylabel("Spending Score (1-100)")
ax2.set_title("Customer Segmentation")
ax2.legend()

st.pyplot(fig2)

# Data preview
st.subheader("📄 Clustered Data Preview")
st.dataframe(filtered_df.head(50), use_container_width=True)

# Download
st.subheader("⬇️ Download Clustered Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="clustered_customers.csv",
    mime="text/csv"
)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit + Matplotlib")