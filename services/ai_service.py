def generate_lighting_recommendation(
    room_type,
    room_size,
    style,
    preferences,
    prompt
):
    """
    Generate a lighting recommendation.

    Temporary fallback response.
    """

    return {
        "recommendedLumens": 3000,
        "colorTemperature": "2700K - Warm White",
        "fixtureTypes": [
            "Chandelier",
            "Floor lamp",
            "Wall sconces"
        ],
        "placement": "Center ceiling, corners for ambient",
        "estimatedCost": 1500
    }