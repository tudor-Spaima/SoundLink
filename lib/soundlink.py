import requests


'''
 $$$$$$\                                      $$\ $$\       $$\           $$\       
$$  __$$\                                     $$ |$$ |      \__|          $$ |      
$$ /  \__| $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$$ |$$ |      $$\ $$$$$$$\  $$ |  $$\ 
\$$$$$$\  $$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$ |$$ |      $$ |$$  __$$\ $$ | $$  |
 \____$$\ $$ /  $$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |$$ |      $$ |$$ |  $$ |$$$$$$  / 
$$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |$$  _$$<  
\$$$$$$  |\$$$$$$  |\$$$$$$  |$$ |  $$ |\$$$$$$$ |$$$$$$$$\ $$ |$$ |  $$ |$$ | \$$\ 
 \______/  \______/  \______/ \__|  \__| \_______|\________|\__|\__|  \__|\__|  \__|
                                                                                    
                                                                                            
'''

class Band:
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
            response = requests.get(base_url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            artist_id = data.get('data', [])[0].get('id')

            similar_url = f'https://api.deezer.com/artist/{artist_id}/related'
            params = {
                'limit': limit,
                'output': 'json'
            }

            response = requests.get(similar_url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            artists = data.get('data', [])

            print(f"Recommended similar bands to '{query}':")
            for i, artist in enumerate(artists[:limit], 1):
                name = artist['name']
                print(f"{i}. {name}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

class Song:
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
            response = requests.get(base_url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            artist_id = data.get('data', [])[0].get('artist', {}).get('id')

            tracks_url = f'https://api.deezer.com/artist/{artist_id}/top'
            params = {
                'limit': limit,
                'output': 'json'
            }

            response = requests.get(tracks_url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            tracks = data.get('data', [])

            print(f"Recommended songs from {query} in order of relevance:")
            recommended_songs = set()
            for i, track in enumerate(tracks[:limit], 1):
                artist = track['artist']['name']
                title = track['title']
                song = f"{artist} - {title}"
                if song not in recommended_songs:
                    print(f"{i}. {song}")
                    recommended_songs.add(song)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")




def get_band_recommendations(query, limit, api_key):
    api_key = api_key
    __recommendation = Band(api_key).recommend_similar_bands(query, limit)
    return __recommendation


def get_song_recommendations(query, limit, api_key):
    api_key = api_key
    __recommendation = Song(api_key).recommend_songs(query, limit)
    return __recommendation
