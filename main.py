import data_preprocessing
import kmeans_clustering
import visualization

# Load data
df = data_preprocessing.load_data()

# Select features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Apply K-Means
clustered_data, model = kmeans_clustering.apply_kmeans(X)

# Visualize results
visualization.plot_clusters(clustered_data)
