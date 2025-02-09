import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(X):
    plt.figure(figsize=(8,5))
    sns.scatterplot(x=X['Annual Income (k$)'], y=X['Spending Score (1-100)'], hue=X['Cluster'], palette="viridis")
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.title('Customer Segmentation')
    plt.show()

if __name__ == "__main__":
    import kmeans_clustering
    clustered_data, _ = kmeans_clustering.apply_kmeans(kmeans_clustering.X)
    plot_clusters(clustered_data)
