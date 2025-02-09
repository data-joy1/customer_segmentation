from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def apply_kmeans(X, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    X['Cluster'] = kmeans.fit_predict(X)
    return X, kmeans

def evaluate_clustering(X, model):
    score = silhouette_score(X, model.labels_)
    print(f"Silhouette Score: {score:.2f}")

if __name__ == "__main__":
    import data_preprocessing
    df = data_preprocessing.load_data()
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    clustered_data, model = apply_kmeans(X)
    print(clustered_data.head())
    clustered_data, model = apply_kmeans(X)
    evaluate_clustering(X, model)
