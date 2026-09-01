import os
import json

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_ai_recommendation(
    room_type,
    room_size,
    style,
    preferences,
    prompt
):
    """
    Generate a lighting recommendation.

    Uses OpenAI through LangChain when an API key is available.
    Otherwise, uses a rule-based fallback.
    """

    # ------------------------------------------------
    # OpenAI + LangChain
    # ------------------------------------------------

    if OPENAI_API_KEY:

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=OPENAI_API_KEY,
            temperature=0.7
        )

        prompt_template = ChatPromptTemplate.from_messages([
            (
                "system",
                """
You are an expert interior lighting designer.

Return ONLY valid JSON.

Use exactly this structure:

{
    "recommendedLumens": 0,
    "colorTemperature": "",
    "fixtureTypes": [],
    "placement": ""
}

Do not include markdown.
Do not include explanations outside the JSON.
"""
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

        try:
            return json.loads(response.content)

        except json.JSONDecodeError:
            raise ValueError(
                "AI returned an invalid JSON response."
            )

    # ------------------------------------------------
    # Rule-based fallback
    # ------------------------------------------------

    room_type = room_type.lower().strip()
    style = style.lower().strip()

    # Brightness recommendation
    room_lighting = {
        "bedroom": 15,
        "living room": 20,
        "kitchen": 35,
        "bathroom": 30,
        "dining room": 20,
        "office": 30
    }

    lumens_per_sqft = room_lighting.get(
        room_type,
        20
    )

    recommended_lumens = int(
        room_size * lumens_per_sqft
    )

    # Color temperature recommendation
    color_temperature = "3000K - Warm White"

    preference_text = " ".join(
        preferences
    ).lower()

    if "warm" in preference_text:
        color_temperature = "2700K - Warm White"

    elif "cool" in preference_text:
        color_temperature = "4000K - Cool White"

    elif "daylight" in preference_text:
        color_temperature = "5000K - Daylight"

    # Fixture recommendations
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
        [
            "Ceiling light",
            "Floor lamp",
            "Wall light"
        ]
    )

    # Placement recommendations
    placement = {
        "bedroom":
            "Center ceiling and beside the bed",

        "living room":
            "Center ceiling with additional lighting near seating areas",

        "kitchen":
            "Ceiling, over work areas and under cabinets",

        "bathroom":
            "Ceiling and around the vanity",

        "dining room":
            "Above the dining table with additional ambient lighting",

        "office":
            "Ceiling and near the work desk"
    }

    recommended_placement = placement.get(
        room_type,
        "Center ceiling and suitable room areas"
    )

    return {
        "recommendedLumens": recommended_lumens,
        "colorTemperature": color_temperature,
        "fixtureTypes": selected_fixtures,
        "placement": recommended_placement
    }