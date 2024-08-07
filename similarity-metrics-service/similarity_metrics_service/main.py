import random
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans

from similarity_metrics_service.constants import *
from similarity_metrics_service.utils import save_json

print("Program started.")

print("Loading data...")
file_path = 'input/songs.csv'
data = pd.read_csv(file_path, encoding='unicode_escape')

# Initial data may include empty fields, so it can cause unexpected behavior.
data.fillna(0, inplace=True)

for feature in FEATURES:
    data[feature] = data[feature].astype(str).str.replace(',', '').astype(float)

print("Normalizing data...")
scaler = StandardScaler()
data_scaled = pd.DataFrame(scaler.fit_transform(data[FEATURES]), columns=FEATURES)

print("Loading model...")
kmeans = KMeans(n_clusters=CLUSTERS_COUNT)
data['Cluster'] = kmeans.fit_predict(data_scaled)

data['Popularity'] = data[FEATURES].sum(axis=1)
scaler = MinMaxScaler(feature_range=(0.3, 1.0))
data['Radius'] = scaler.fit_transform(data[['Popularity']])

print("Creating nodes...")
nodes = []
cluster_areas = []
cluster_width = WINDOW_WIDTH // CLUSTERS_COUNT
cluster_height = WINDOW_HEIGHT // CLUSTERS_COUNT

for cluster_id in range(CLUSTERS_COUNT):
    x_min = (cluster_id % (WINDOW_WIDTH // cluster_width)) * cluster_width
    y_min = (cluster_id // (WINDOW_WIDTH // cluster_width)) * cluster_height
    x_max = x_min + cluster_width
    y_max = y_min + cluster_height
    cluster_areas.append((x_min, y_min, x_max, y_max))

for index, row in data.iterrows():
    cluster_id = row['Cluster']
    x_min, y_min, x_max, y_max = cluster_areas[cluster_id]
    nodes.append({
        "name": row["Track"],
        "cluster": row["Cluster"],
        "radius": row["Radius"],
        "x": random.uniform(x_min, x_max),
        "y": random.uniform(y_min, y_max)
    })

save_json(nodes, "nodes.json")

print("Creating links...")
links = []
similarity_matrix = cosine_similarity(data_scaled)
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if similarity_matrix[i, j] > 0.8:
            links.append({
                "from": data.iloc[i]["Track"],
                "to": data.iloc[j]["Track"]
            })

save_json(links, "links.json")

print("Program finished.")
