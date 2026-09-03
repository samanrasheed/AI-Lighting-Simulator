def create_lighting_prompt(room_type, room_size, style, preferences):
    prompt = f"""
You are an expert interior lighting designer.

Task:
Recommend the best lighting setup for the given room.

Room Type:
{room_type}

Room Size:
{room_size} square meters

Interior Style:
{style}

User Preferences:
{', '.join(preferences) if preferences else 'None'}

Requirements:

1. Recommend an appropriate brightness level in lumens.
2. Recommend a suitable color temperature.
3. Recommend suitable lighting fixture types.
4. Suggest suitable placement for the lighting fixtures.
5. Consider the room type, room size, interior style, and user preferences.
6. Return ONLY valid JSON.
7. Do not include any explanation outside the JSON.

Expected JSON structure:

{{
    "recommendedLumens": 0,
    "colorTemperature": "",
    "fixtureTypes": [],
    "placement": ""
}}
"""

    return prompt