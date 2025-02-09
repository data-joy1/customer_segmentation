Customer Segmentation using K-Means Clustering
📌 Project Overview
Customer segmentation is an unsupervised learning task used to group similar customers based on their purchasing behavior. This project uses the K-Means clustering algorithm to segment customers based on their Annual Income and Spending Score.

📂 Project Structure
📂 customer_segmentation/
├── 📄 data_preprocessing.py  # Load & preprocess data
├── 📄 kmeans_clustering.py   # Apply K-Means clustering
├── 📄 visualization.py       # Generate visualizations
├── 📄 main.py               # Run the full pipeline
├── 📄 requirements.txt      # Dependencies list
├── 📄 README.md             # Project documentation
├── 📄 Mall_Customers.csv    # Dataset (if applicable)

🛠️ Technologies Used
Programming Language: Python
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
Machine Learning Algorithm: K-Means Clustering

📊 Dataset Used
Source: Kaggle - Mall Customers Dataset
Features:
✅ CustomerID – Unique customer identifier
✅ Age – Customer’s age
✅ Annual Income (k$) – Yearly income in thousands
✅ Spending Score (1-100) – Customer spending behavior

📌 Steps to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/data-joy1/customer_segmentation.git
cd customer_segmentation

2️⃣ Run the Project
python main.py

📊 Key Features & Results
✅ Elbow Method to find the optimal number of clusters.
✅ K-Means Clustering to group customers based on spending patterns.
✅ Data Visualization using Seaborn & Matplotlib.

