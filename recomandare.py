import requests
import warnings

class BandRecommendation:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def recommend_similar_bands(self, query, limit=10):
        base_url = 'https://api.deezer.com/search/artist'
        params = {
            'q': query,
            'output': 'json',
            'limit': 1  # Limit to 1 result for the initial query
        }

        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = requests.get(base_url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            artist_id = data.get('data', [])[0].get('id')

            similar_url = f'https://api.deezer.com/artist/{artist_id}/related'
            params['limit'] = limit

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = requests.get(similar_url, params=params, headers=self.headers)
            response.raise_for_status()

            artists = data.get('data', [])

            print(f"Recommended similar bands to '{query}':")
            for i, artist in enumerate(artists, 1):
                name = artist['name']
                print(f"{i}. {name}")
        except Exception as e:
            print(f"An error occurred: {e}")

class SongRecommendation:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def recommend_songs(self, query, limit=10):
        base_url = 'https://api.deezer.com/search'
        params = {
            'q': query,
            'output': 'json',
            'limit': 1
        }

        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = requests.get(base_url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            artist_id = data.get('data', [])[0].get('artist', {}).get('id')

            tracks_url = f'https://api.deezer.com/artist/{artist_id}/top'
            params = {
                'limit': limit,
                'output': 'json'
            }

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = requests.get(tracks_url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            tracks = data.get('data', [])

            print(f"Recommended songs from {query} in order of relevance:")
            recommended_songs = set()
            for i, track in enumerate(tracks, 1):
                artist = track['artist']['name']
                title = track['title']
                song = f"{artist} - {title}"
                if song not in recommended_songs:
                    print(f"{i}. {song}")
                    recommended_songs.add(song)
                    if len(recommended_songs) == limit:
                        break
        except Exception as e:
            print(f"An error occurred: {e}")
