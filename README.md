🧠 CustomerScope – Customer Segmentation with Machine Learning

CustomerScope is a machine learning project that analyzes customer data and performs customer segmentation using clustering techniques. The goal is to group customers based on their purchasing behavior and demographics, helping businesses better understand customer profiles and tailor marketing strategies.


🚀 Features
	•	📊 Exploratory Data Analysis (EDA) on customer dataset
	•	🧹 Data preprocessing & feature scaling
	•	🤖 Unsupervised learning using K-Means clustering
	•	📈 Visualizations of customer clusters
	•	🌐 Interactive Streamlit web app to explore clusters
	•	📁 Clean modular project structure
<img width="1159" height="491" alt="image" src="https://github.com/user-attachments/assets/e27bd57e-7f91-400c-9e46-ae634005f0ea" />
<img width="847" height="721" alt="image" src="https://github.com/user-attachments/assets/98ec59fa-5056-4380-9c21-187fcd385f86" />
<img width="809" height="698" alt="image" src="https://github.com/user-attachments/assets/f715dfc1-4d0c-4cf3-b25d-1370bbe754a6" />
<img width="857" height="612" alt="image" src="https://github.com/user-attachments/assets/fd09a188-030b-4f1f-88a3-ad4401e5ca16" />


🗂️ Project Structure

CustomerScope/
│
├── data/
│   └── Mall_Customers.csv
│
├── outputs/
│   └── clustered_customers.csv
│
├── src/
│   ├── eda.py
│   ├── preprocess.py
│   ├── train.py
│   └── visualize.py
│
├── app.py
├── requirements.txt
└── README.md



⚙️ Installation

git clone https://github.com/Hassanmahmood4/CustomerScope.git
cd CustomerScope
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt



▶️ How to Run (Step-by-Step)

1️⃣ Run EDA

python src/eda.py

2️⃣ Preprocess the Data

python src/preprocess.py

3️⃣ Train Clustering Model

python src/train.py

4️⃣ Visualize Clusters

python src/visualize.py

5️⃣ Launch Web App

streamlit run app.py


📊 Dataset

This project uses the Mall Customers dataset, containing:
	•	Customer ID
	•	Age
	•	Annual Income
	•	Spending Score

Source: Kaggle / public dataset.


🧠 ML Approach
	•	Algorithm: K-Means Clustering
	•	Distance Metric: Euclidean
	•	Objective: Segment customers into meaningful groups
	•	Evaluation: Visual cluster separation

🎯 Use Cases
	•	Customer segmentation
	•	Targeted marketing strategies
	•	Business intelligence dashboards
	•	Retail analytics


🛠 Tech Stack
	•	Python
	•	Pandas
	•	NumPy
	•	Scikit-learn
	•	Matplotlib
	•	Streamlit


📌 Future Improvements
	•	Add automatic cluster labeling
	•	Add customer profile summaries
	•	Deploy on Streamlit Cloud
	•	Try DBSCAN / Hierarchical clustering
	•	Add CSV upload in UI


👨‍💻 Author

Hassan Mahmood
GitHub: https://github.com/Hassanmahmood4


If you want, I can also give you:
	•	A 2-line GitHub description
	•	A project poster
	•	A demo video script
	•	A LinkedIn post caption
