from flask import Flask, request, jsonify
from flask_cors import CORS

from services.prompt_service import create_lighting_prompt
from services.ai_service import generate_lighting_recommendation

from validators.request_validator import validate_lighting_request

from utils.response import success_response, error_response
from utils.logger import logger


app = Flask(__name__)

# Enable CORS
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to AI Lighting Simulator API",
        "status": "running"
    })


@app.route("/api/ai/simulate-lighting", methods=["POST"])
def simulate_lighting():

    logger.info("Lighting Simulator API called")

    data = request.get_json()

    logger.info("Request data received")

    # Validate request
    validation_error = validate_lighting_request(data)

    if validation_error:
        logger.error(
            f"Validation failed: {validation_error['error']}"
        )

        return jsonify(
            error_response(validation_error["error"])
        ), 400

    logger.info("Validation successful")

    # Extract request data
    room_type = data.get("roomType").strip().lower()
    room_size = data.get("roomSize")
    style = data.get("style").strip().lower()
    preferences = data.get("preferences", [])

    # Create AI prompt
    prompt = create_lighting_prompt(
        room_type,
        room_size,
        style,
        preferences
    )

    logger.info("Lighting prompt created successfully")

    try:

        # Generate lighting recommendation
        result = generate_lighting_recommendation(
            room_type=room_type,
            room_size=room_size,
            style=style,
            preferences=preferences,
            prompt=prompt
        )

        logger.info(
            "Lighting recommendation generated successfully"
        )

        return jsonify(
            success_response(result)
        )

    except Exception as e:

        logger.exception(
            f"Lighting Service Error: {e}"
        )

        return jsonify(
            error_response(
                "Unable to generate lighting recommendation "
                "at the moment. Please try again later."
            )
        ), 500


if __name__ == "__main__":
    app.run(debug=True)

