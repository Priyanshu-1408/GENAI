from dotenv import load_dotenv
from mem0 import Memory
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

config = {
    "version": "v1.1",

    "embedder": {
        "provider": "gemini",
        "config": {
            "api_key": GOOGLE_API_KEY,
            "model": "text-embedding-004"
        }
    },

    "llm": {
        "provider": "gemini",
        "config": {
            "api_key": GOOGLE_API_KEY,
            "model": "gemini-2.5-flash"
        }
    },

    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": "neo4j+s://fd10af2d.databases.neo4j.io",
            "username": "neo4j",
            "password": "YOUR_PASSWORD"
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