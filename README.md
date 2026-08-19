# AI Lighting Simulator

A Flask-based backend API for an AI Lighting Simulator that provides lighting recommendations based on room type, room size, interior style, and user preferences.

## Project Overview

The AI Lighting Simulator is designed to recommend suitable lighting configurations for different room environments.

The assigned backend task includes:

- Lighting simulation recommendations
- Recommended brightness/lumens
- Color temperature recommendations
- Suitable lighting fixture types
- Suggested fixture placement
- Estimated lighting cost

The project is being developed as a REST API using Python and Flask.

## Current Project Status

### Completed

- Project structure created
- Python virtual environment configured
- Flask and required backend dependencies installed
- Request validation implemented
- Standard success and error response structure implemented
- Application logging configured
- Lighting recommendation prompt service created
- Git repository initialized

### In Progress

- Flask API endpoint implementation
- Local API testing with Postman
- AI service integration

### Planned

- Connect the AI service
- Add environment variable/API key configuration
- Test AI-generated lighting recommendations
- Add fallback handling for AI service failures
- Push daily development updates to GitHub
- Deploy the API when the implementation is complete

## API Endpoint

The project documentation specifies the following endpoint:

```text
POST /api/ai/simulate-lighting
```

## Request Format

The expected request contains:

```json
{
  "roomType": "living room",
  "roomSize": 30,
  "style": "modern",
  "preferences": [
    "warm",
    "dimmable"
  ]
}
```

### Request Fields

| Field | Description |
|---|---|
| `roomType` | Type of room being simulated |
| `roomSize` | Room size |
| `style` | Interior style |
| `preferences` | User lighting preferences |

## Expected Response

The project documentation provides the following response structure:

```json
{
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
```

## Validation

The API validates the incoming lighting request before processing it.

Current validation includes:

- Room type is required
- Room type must be supported
- Room size is required
- Room size must be a positive number
- Interior style is required
- Interior style must be supported
- Preferences must be provided as a list

## Project Structure

```text
18Aug_2026_Saman_AI_Lighting_Simulator/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── services/
│   ├── prompt_service.py
│   └── ai_service.py
│
├── validators/
│   └── request_validator.py
│
└── utils/
    ├── response.py
    └── logger.py
```

## Technologies Used

- Python 3.9.6
- Flask
- Flask-CORS
- Gunicorn
- REST API
- Git & GitHub
- Postman for API testing

## Local Setup

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Development Workflow

The project is being developed incrementally, with daily progress pushed to GitHub.

Typical workflow:

```bash
git status
git add .
git commit -m "Describe the work completed"
git push
```

## Current Development Progress

- Created the AI Lighting Simulator project
- Created the project directory structure
- Created Python virtual environment
- Installed Flask, Flask-CORS, and Gunicorn
- Created request validation module
- Created common API response utilities
- Created application logger
- Created lighting recommendation prompt service
- Initialized Git repository

## Testing

The API will be tested locally using Postman after the Flask endpoint is implemented.

Testing will include:

- Valid lighting requests
- Missing room information
- Invalid room types
- Invalid room sizes
- Invalid styles
- Invalid preference formats
- Successful lighting recommendations
- AI service fallback handling

## Deployment

Deployment will be completed after the API and AI integration have been tested successfully.

The final deployed API URL will be added to this README once deployment is completed.

## Project Goal

The goal of the AI Lighting Simulator backend is to provide lighting recommendations based on room characteristics and user preferences, including brightness, color temperature, fixture types, placement, and estimated cost.