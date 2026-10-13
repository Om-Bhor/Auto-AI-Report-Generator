import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_URL = "https://google.serper.dev/search"


def search_company(topic):
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "q": topic
    }

    response = requests.post(
        SERPER_URL,
        headers=headers,
        json=payload
    )

    return response.json()

