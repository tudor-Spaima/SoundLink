from soundlink import get_band_recommendations, get_song_recommendations

query = 'Pink Floyd'
limit = 10
api_key= 'API_KEY'


def main():
    band_recommendations = get_band_recommendations(query, limit, api_key)

    '''if you want to get song recommendations from a certain band or artist:'''
    #song_recommendations = get_song_recommendations(query, limit)

if __name__ == '__main__':
    main()
