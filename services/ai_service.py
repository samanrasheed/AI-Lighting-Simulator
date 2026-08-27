import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_ai_recommendation(prompt):
    """
    Generate a lighting recommendation using OpenAI through LangChain.

    This function is only used when an API key is available.
    """

    if not OPENAI_API_KEY:
        return None

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY,
        temperature=0.7
    )

    prompt_template = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an AI lighting design assistant. "
            "Provide practical lighting recommendations."
        ),
        (
            "human",
            "{prompt}"
        )
    ])

    chain = prompt_template | llm

    response = chain.invoke({
        "prompt": prompt
    })

    return response.content


def generate_lighting_recommendation(
    room_type,
    room_size,
    style,
    preferences,
    prompt
):
    """
    Generate a lighting recommendation.

    If an OpenAI API key is available, the AI integration can be used.
    Otherwise, use the rule-based fallback.
    """

    # Try AI recommendation when an API key is available
    if OPENAI_API_KEY:
        ai_result = generate_ai_recommendation(prompt)

        if ai_result:
            return {
                "roomType": room_type,
                "roomSize": room_size,
                "style": style,
                "preferences": preferences,
                "aiRecommendation": ai_result
            }

    # Rule-based fallback
    room_type = room_type.lower().strip()
    style = style.lower().strip()

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

    color_temperature = "3000K - Warm White"

    preference_text = " ".join(preferences).lower()

    if "warm" in preference_text:
        color_temperature = "2700K - Warm White"
    elif "cool" in preference_text:
        color_temperature = "4000K - Cool White"
    elif "daylight" in preference_text:
        color_temperature = "5000K - Daylight"

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

    placement = {
        "bedroom": "Center ceiling and beside the bed",
        "living room": (
            "Center ceiling with additional lighting "
            "near seating areas"
        ),
        "kitchen": (
            "Ceiling, over work areas and under cabinets"
        ),
        "bathroom": "Ceiling and around the vanity",
        "dining room": (
            "Above the dining table with additional "
            "ambient lighting"
        ),
        "office": "Ceiling and near the work desk"
    }

    recommended_placement = placement.get(
        room_type,
        "Center ceiling and suitable room corners"
    )

    style_notes = {
        "modern": (
            "Use clean and minimal fixtures "
            "with simple designs."
        ),
        "minimal": (
            "Use simple fixtures with minimal "
            "visual clutter."
        ),
        "traditional": (
            "Use decorative fixtures with warm "
            "ambient lighting."
        ),
        "industrial": (
            "Use metal fixtures and exposed-style "
            "lighting."
        ),
        "luxury": (
            "Use statement fixtures with layered "
            "ambient lighting."
        )
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
        "styleRecommendation": recommendation_note,
        "estimatedCost": 1500
    }