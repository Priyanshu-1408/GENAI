from dotenv import load_dotenv
from mem0 import Memory
from google import genai
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini Client
client = genai.Client(api_key=GOOGLE_API_KEY)

config = {
    "version": "v1.1",

    "embedder": {
        "provider": "gemini",
        "config": {
            "api_key": GOOGLE_API_KEY,
            "model": "models/gemini-embedding-001"
        }
    },

    "llm": {
        "provider": "gemini",
        "config": {
            "api_key": GOOGLE_API_KEY,
            "model": "gemini-2.5-flash"
        }
    },

    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

mem_client = Memory.from_config(config)

user_query = input("> ")

# Gemini Response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_query
)

ai_response = response.text

print("AI:", ai_response)

# Save Conversation
mem_client.add(
    [
        {"role": "user", "content": user_query},
        {"role": "assistant", "content": ai_response},
    ],
    user_id="priyanshu",
)

print("Memory has been saved...")