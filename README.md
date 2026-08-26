# AI Lighting Simulator

## Project Overview

AI Lighting Simulator is a Flask-based backend API designed to simulate lighting recommendations for different room types.

The system analyzes room information such as room type, room size, interior style, and lighting preferences to recommend suitable:

- Brightness / lumens
- Color temperature
- Lighting fixture types
- Fixture placement
- Style-based lighting recommendations

The project is being developed as part of an AI-powered lighting simulation system.

---

## Current Features

### 1. Room-Based Lighting Recommendations

The system provides different lighting recommendations based on the selected room.

Supported room types include:

- Bedroom
- Living Room
- Kitchen
- Bathroom
- Dining Room
- Office

### 2. Brightness Recommendation

Recommended brightness is calculated according to room type and room size.

Different rooms use different lumen-per-square-foot values.

For example:

- Bedroom → 15 lumens per square foot
- Living Room → 20 lumens per square foot
- Kitchen → 35 lumens per square foot
- Bathroom → 30 lumens per square foot
- Dining Room → 20 lumens per square foot
- Office → 30 lumens per square foot

### 3. Color Temperature Recommendation

The system adjusts the recommended color temperature based on user preferences.

Examples:

- Warm → 2700K Warm White
- Cool → 4000K Cool White
- Daylight → 5000K Daylight

### 4. Fixture Recommendations

The system recommends suitable fixture types depending on the room.

Examples include:

- Ceiling lights
- Floor lamps
- Wall sconces
- Pendant lights
- Chandeliers
- Under-cabinet lights
- Desk lamps
- Task lighting

### 5. Placement Recommendations

The system also provides suggested locations for lighting fixtures.

For example:

- Bedroom → Center ceiling and beside the bed
- Living room → Center ceiling and seating areas
- Kitchen → Ceiling, work areas, and under cabinets
- Bathroom → Ceiling and vanity area
- Office → Ceiling and work desk

### 6. Style Recommendations

Lighting recommendations can also take the room style into consideration.

Supported styles include:

- Modern
- Minimal
- Traditional
- Industrial
- Luxury

---

## API

### Simulate Lighting

**POST**

```text
/api/ai/simulate-lighting
```

### Request Example

```json
{
    "roomType": "bedroom",
    "roomSize": 20,
    "style": "modern",
    "preferences": ["warm"]
}
```

### Example Response

```json
{
    "roomType": "bedroom",
    "roomSize": 20,
    "style": "modern",
    "recommendedLumens": 300,
    "colorTemperature": "2700K - Warm White",
    "fixtureTypes": [
        "Ceiling light",
        "Bedside lamps",
        "Wall sconces"
    ],
    "placement": "Center ceiling and beside the bed",
    "styleRecommendation": "Use clean and minimal fixtures with simple designs."
}
```

---

## Project Architecture

```text
AI Lighting Simulator
│
├── app.py
│
├── services/
│   ├── prompt_service.py
│   └── ai_service.py
│
├── validators/
│   └── request_validator.py
│
├── utils/
│   ├── response.py
│   └── logger.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## Request Flow

```text
Client / Postman
       │
       ▼
     app.py
       │
       ▼
Request Validation
       │
       ▼
prompt_service.py
       │
       ▼
ai_service.py
       │
       ▼
Lighting Recommendation
       │
       ▼
JSON Response
```

---

## Technologies Used

- Python 3.9.6
- Flask
- Flask-CORS
- REST API
- JSON
- Git & GitHub
- Postman

---

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project directory

```bash
cd 18Aug_2026_Saman_AI_Lighting_Simulator
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

The API will run locally on:

```text
http://127.0.0.1:5000
```

---

## Testing

The API can be tested using Postman.

Example endpoint:

```text
POST http://127.0.0.1:5000/api/ai/simulate-lighting
```

Select:

```text
Body → raw → JSON
```

Then provide:

```json
{
    "roomType": "kitchen",
    "roomSize": 30,
    "style": "minimal",
    "preferences": ["cool"]
}
```

Click **Send** to test the API.

---

## Current Development Status

### Completed

- Flask API setup
- CORS configuration
- Request validation
- Response handling
- Logging setup
- Prompt service structure
- Lighting recommendation service
- Room-based lumen calculation
- Color temperature recommendations
- Fixture recommendations
- Lighting placement recommendations
- Style-based recommendations
- Local API testing with Postman

### In Progress

- AI-powered recommendation integration
- Advanced lighting simulation
- Dynamic AI-generated recommendations
- Production deployment

---

## Future Improvements

The project can be extended with:

- AI-generated lighting recommendations
- More room types
- More interior styles
- Advanced brightness calculations
- Dynamic color-temperature recommendations
- Multiple lighting layers such as ambient, task, and accent lighting
- Energy-efficient lighting suggestions
- Cost estimation
- Real-time lighting simulation
- Frontend integration
- Production deployment

---

## Development

This project is being developed incrementally, with features tested locally using Flask and Postman before deployment.

## License

This project is developed for internship/project purposes.