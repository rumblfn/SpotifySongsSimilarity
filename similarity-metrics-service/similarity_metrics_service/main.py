import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans

from similarity_metrics_service.constants import FEATURES, CLUSTERS_COUNT
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
for index, row in data.iterrows():
    nodes.append({
        "name": row["Track"],
        "cluster": row["Cluster"],
        "radius": row["Radius"],
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
