import os
import requests
from dotenv import load_dotenv

load_dotenv()

PERSPECTIVE_API_KEY = os.getenv("PERSPECTIVE_API_KEY")
PERSPECTIVE_URL = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"

def evaluate_toxicity_perspective(text):
    if not PERSPECTIVE_API_KEY:
        raise Exception("Missing Perspective API Key")

    data = {
        "comment": {"text": text},
        "languages": ["en"],
        "requestedAttributes": {"TOXICITY": {}}
    }

    response = requests.post(
        url=f"{PERSPECTIVE_URL}?key={PERSPECTIVE_API_KEY}",
        json=data
    )

    result = response.json()
    score = result["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
    return score
