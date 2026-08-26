import os
from dotenv import load_dotenv

load_dotenv() #read .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_lighting_recommendation(
    room_type,
    room_size,
    style,
    preferences,
    prompt
):
    """
    Generate a lighting recommendation based on room details.
    """

    room_type = room_type.lower().strip()
    style = style.lower().strip()

    # Calculate recommended lumens based on room size
    if room_type == "bedroom":
        lumens_per_sqft = 15
    elif room_type == "living room":
        lumens_per_sqft = 20
    elif room_type == "kitchen":
        lumens_per_sqft = 35
    elif room_type == "bathroom":
        lumens_per_sqft = 30
    elif room_type == "dining room":
        lumens_per_sqft = 20
    elif room_type == "office":
        lumens_per_sqft = 30
    else:
        lumens_per_sqft = 20

    recommended_lumens = int(room_size * lumens_per_sqft)

    # Default lighting
    color_temperature = "3000K - Warm White"

    # Adjust color temperature according to preferences
    preference_text = " ".join(preferences).lower()

    if "warm" in preference_text:
        color_temperature = "2700K - Warm White"
    elif "cool" in preference_text:
        color_temperature = "4000K - Cool White"
    elif "daylight" in preference_text:
        color_temperature = "5000K - Daylight"

    # Recommend fixture types according to room
    fixture_types = {
        "bedroom": [
            "Ceiling light",
            "Bedside lamps",
            "Wall sconces"
        ],
        "living room": [
            "Ceiling light",
            "Floor lamp",
            "Wall sconces"
        ],
        "kitchen": [
            "Ceiling light",
            "Pendant lights",
            "Under-cabinet lights"
        ],
        "bathroom": [
            "Ceiling light",
            "Vanity lights",
            "Wall sconces"
        ],
        "dining room": [
            "Pendant light",
            "Chandelier",
            "Wall sconces"
        ],
        "office": [
            "Ceiling light",
            "Desk lamp",
            "Task lighting"
        ]
    }

    selected_fixtures = fixture_types.get(
        room_type,
        ["Ceiling light", "Floor lamp", "Wall light"]
    )

    # Placement recommendations
    placement = {
        "bedroom": "Center ceiling and beside the bed",
        "living room": "Center ceiling with additional lighting near seating areas",
        "kitchen": "Ceiling, over work areas and under cabinets",
        "bathroom": "Ceiling and around the vanity",
        "dining room": "Above the dining table with additional ambient lighting",
        "office": "Ceiling and near the work desk"
    }

    recommended_placement = placement.get(
        room_type,
        "Center ceiling and suitable room corners"
    )

    # Style-based recommendation
    style_notes = {
        "modern": "Use clean and minimal fixtures with simple designs.",
        "minimal": "Use simple fixtures with minimal visual clutter.",
        "traditional": "Use decorative fixtures with warm ambient lighting.",
        "industrial": "Use metal fixtures and exposed-style lighting.",
        "luxury": "Use statement fixtures with layered ambient lighting."
    }

    recommendation_note = style_notes.get(
        style,
        "Choose fixtures that complement the room style."
    )

    return {
        "roomType": room_type,
        "roomSize": room_size,
        "style": style,
        "recommendedLumens": recommended_lumens,
        "colorTemperature": color_temperature,
        "fixtureTypes": selected_fixtures,
        "placement": recommended_placement,
        "styleRecommendation": recommendation_note
    }