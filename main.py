import requests

def recommend_similar_bands(api_key, query, limit=10):
    # Build the request URL
    base_url = 'https://api.deezer.com/search/artist'
    params = {
        'q': query,
        'output': 'json',
        'limit': 1  # Limit to 1 result for the initial query
    }
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Send the GET request to the API for the initial query
    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        data = response.json()
        
        # Extract the artist ID from the response
        artist_id = data.get('data', [])[0].get('id')
        
        # Build the request URL for similar artists
        similar_url = f'https://api.deezer.com/artist/{artist_id}/related'
        params['limit'] = limit  # Retrieve "limit" similar artists
        
        # Send the GET request to the API for similar artists
        response = requests.get(similar_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        data = response.json()
        
        # Extract the similar artists from the response
        artists = data.get('data', [])
        
        # Print the recommended similar artists in the order of similarity
        print(f"Recommended similar bands to '{query}':")
        for i, artist in enumerate(artists, 1):
            name = artist['name']
            print(f"{i}. {name}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

api_key = '79f636998b7825c8adb2a900f9619e39'
query = input("Enter a band or artist name: ")
limit = int(input("Enter the number of similar bands to recommend: "))

recommend_similar_bands(api_key, query, limit)

