from band_recommendation import BandRecommendation

def get_recommendations(query, limit):
    api_key = '79f636998b7825c8adb2a900f9619e39'
    recommendation = BandRecommendation(api_key).recommend_similar_bands(query, limit)
    return recommendation
