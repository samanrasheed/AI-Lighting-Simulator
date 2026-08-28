import os

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

    If an OpenAI API key is available, use LangChain/OpenAI.
    Otherwise, use the rule-based fallback.
    """

    # AI recommendation
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

The JSON must contain exactly these fields:

{
    "recommendedLumens": 0,
    "colorTemperature": "",
    "fixtureTypes": [],
    "placement": "",
    "estimatedCost": 0
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

        return response.content

    # ------------------------------------------------
    # Rule-based fallback when API key is unavailable
    # ------------------------------------------------

    room_type = room_type.lower().strip()
    style = style.lower().strip()

       # Brightness calculation
    room_lighting = {
        "bedroom": {
           "lumens_per_sqft": 15,
           "fixtures": 3
    },
        "living room": {
         "lumens_per_sqft": 20,
         "fixtures": 4
    },
      "kitchen": {
        "lumens_per_sqft": 35,
        "fixtures": 5
    },
     "bathroom": {
        "lumens_per_sqft": 30,
        "fixtures": 3
    },
     "dining room": {
        "lumens_per_sqft": 20,
        "fixtures": 3
    },
     "office": {
        "lumens_per_sqft": 30,
        "fixtures": 4
    }
}

    lighting_info = room_lighting.get(
    room_type,
    {
        "lumens_per_sqft": 20,
        "fixtures": 3
    }
)

    recommended_lumens = int(
        room_size * lighting_info["lumens_per_sqft"]
)

    recommended_fixture_count = lighting_info["fixtures"]
    # Color temperature
    color_temperature = "3000K - Warm White"

    preference_text = " ".join(preferences).lower()

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

    # Style recommendations
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

    # Estimated cost
    estimated_cost = 1500

    return {
        "roomType": room_type,
        "roomSize": room_size,
        "style": style,
        "recommendedFixtureCount": recommended_fixture_count,
        "recommendedLumens": recommended_lumens,
        "colorTemperature": color_temperature,
        "fixtureTypes": selected_fixtures,
        "placement": recommended_placement,
        "styleRecommendation": recommendation_note,
        "estimatedCost": estimated_cost
    }