# src/core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        # --- NEW LINE ADD KAREIN ---
        self.OPENAI_API_KEY: str = self._get_required_env("OPENAI_API_KEY")
        # ---------------------------
        
        self.GEMINI_API_KEY: str = self._get_required_env("GEMINI_API_KEY")
        self.QDRANT_URL: str = self._get_required_env("QDRANT_URL")
        self.QDRANT_API_KEY: str = self._get_required_env("QDRANT_API_KEY")
        self.NEON_DB_URL: str = self._get_required_env("NEON_DB_URL")
        self.API_KEY: str = self._get_required_env("API_KEY")

    def _get_required_env(self, key: str) -> str:
        value = os.getenv(key)
        if not value:
            # Agar variable na mile to error na dein (Development ke liye), ya raise karein
            # Hum safe side rehne ke liye raise kar rahe hain
            raise ValueError(f"Required environment variable '{key}' is not set.")
        return value

settings = Settings()