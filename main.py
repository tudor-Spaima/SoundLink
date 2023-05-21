from recomandare import BandRecommendation, SongRecommendation

api_key = '79f636998b7825c8adb2a900f9619e39'
query = input("Enter a band or artist name: ")
limit = int(input("Enter the number of similar bands to recommend: "))

band_rec = BandRecommendation(api_key)
band_rec.recommend_similar_bands(query, limit)

