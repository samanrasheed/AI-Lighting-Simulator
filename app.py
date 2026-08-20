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