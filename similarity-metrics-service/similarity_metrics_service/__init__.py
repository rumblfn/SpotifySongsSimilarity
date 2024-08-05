import pandas as pd
from sklearn.preprocessing import StandardScaler

# Read data.
file_path = 'songs.csv'
data = pd.read_csv(file_path, encoding='unicode_escape')

# Attributes for similarity.
features = [
    "Spotify Streams", "Spotify Playlist Count", "Spotify Playlist Reach",
    "Spotify Popularity", "YouTube Views", "YouTube Likes", "TikTok Posts",
    "TikTok Likes", "TikTok Views", "YouTube Playlist Reach",
    "Apple Music Playlist Count", "AirPlay Spins", "SiriusXM Spins",
    "Deezer Playlist Count", "Deezer Playlist Reach", "Amazon Playlist Count",
    "Pandora Streams", "Pandora Track Stations", "Soundcloud Streams",
    "Shazam Counts", "TIDAL Popularity"
]

# Initial data may include empty fields, so it can cause unexpected behavior.
data.fillna(0, inplace=True)

for feature in features:
    data[feature] = data[feature].astype(str).str.replace(',', '').astype(float)

scaler = StandardScaler()
data_scaled = pd.DataFrame(scaler.fit_transform(data[features]), columns=features)

print(data_scaled.head())
