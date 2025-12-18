# src/core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        # OpenAI Key
        self.OPENAI_API_KEY: str = self._get_required_env("OPENAI_API_KEY")
        
        # Baqi Keys
        self.GEMINI_API_KEY: str = self._get_required_env("GEMINI_API_KEY")
        self.QDRANT_URL: str = self._get_required_env("QDRANT_URL")
        self.QDRANT_API_KEY: str = self._get_required_env("QDRANT_API_KEY")
        self.NEON_DB_URL: str = self._get_required_env("NEON_DB_URL")
        self.API_KEY: str = self._get_required_env("API_KEY")
        
        # --- YE LINE MISSING THI (CRASH FIX) ---
        # Isay wapas daal dein taake 'content.py' crash na ho
        self.GEMINI_BASE_URL: str = "https://generativelanguage.googleapis.com/v1beta/openai/"

    def _get_required_env(self, key: str) -> str:
        value = os.getenv(key)
        if not value:
            # Safe side rehne ke liye raise kar rahe hain
            raise ValueError(f"Required environment variable '{key}' is not set.")
        return value

settings = Settings()