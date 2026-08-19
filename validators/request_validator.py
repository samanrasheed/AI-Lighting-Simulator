VALID_ROOM_TYPES = [
    "living room",
    "bedroom",
    "kitchen",
    "dining room",
    "bathroom",
    "office"
]

VALID_STYLES = [
    "modern",
    "minimal",
    "traditional",
    "contemporary"
]


def validate_lighting_request(data):

    if not data:
        return {
            "error": "Request body is required."
        }

    # Room type
    room_type = data.get("roomType", "").strip().lower()

    if not room_type:
        return {
            "error": "Room type is required."
        }

    if room_type not in VALID_ROOM_TYPES:
        return {
            "error": "Invalid room type."
        }

    # Room size
    room_size = data.get("roomSize")

    if room_size is None:
        return {
            "error": "Room size is required."
        }

    if not isinstance(room_size, (int, float)) or room_size <= 0:
        return {
            "error": "Room size must be a positive number."
        }

    # Style
    style = data.get("style", "").strip().lower()

    if not style:
        return {
            "error": "Style is required."
        }

    if style not in VALID_STYLES:
        return {
            "error": "Invalid style."
        }

    # Preferences
    preferences = data.get("preferences", [])

    if not isinstance(preferences, list):
        return {
            "error": "Preferences must be provided as a list."
        }

    return None