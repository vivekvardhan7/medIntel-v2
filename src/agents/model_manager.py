import groq
import streamlit as st
from enum import Enum
import logging
import time

logger = logging.getLogger(__name__)

class ModelTier(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    TERTIARY = "tertiary"
    FALLBACK = "fallback"

class ModelManager:
    """
    Manages AI model selection, fallback, and rate limits.
    """

    MODEL_CONFIG = {
        ModelTier.PRIMARY: {
            "provider": "groq",
            "model": "llama3-70b-8192",
            "max_tokens": 2000,
            "temperature": 0.7
        },
        ModelTier.SECONDARY: {
            "provider": "groq",
            "model": "llama3-8b-8192",
            "max_tokens": 2000,
            "temperature": 0.7
        },
        ModelTier.TERTIARY: {
            "provider": "groq",
            "model": "mixtral-8x7b-32768",
            "max_tokens": 2000,
            "temperature": 0.7
        },
        ModelTier.FALLBACK: {
            "provider": "groq",
            "model": "gemma-7b-it",
            "max_tokens": 2000,
            "temperature": 0.7
        }
    }

    def __init__(self):
        self.clients = {}
        self._initialize_clients()

    def _initialize_clients(self):
        """Initialize API clients for each provider."""
        try:
            self.clients["groq"] = groq.Groq(api_key=st.secrets["GROQ_API_KEY"])
        except Exception as e:
            logger.error(f"Failed to initialize Groq client: {str(e)}")
            st.error(f"Groq initialization failed: {e}")

    def generate_analysis(self, data, system_prompt, retry_count=0):
        """
        Generate analysis using the best available model with automatic fallback.
        """
        if retry_count > 3:
            return {"success": False, "error": "All models failed after multiple retries"}

        # Select model tier based on retry
        tier = list(ModelTier)[retry_count]
        model_config = self.MODEL_CONFIG[tier]
        provider = model_config["provider"]
        model = model_config["model"]

        if provider not in self.clients:
            logger.error(f"No client available for provider: {provider}")
            return self.generate_analysis(data, system_prompt, retry_count + 1)

        try:
            client = self.clients[provider]
            logger.info(f"Using {provider}/{model} for generation")

            # Ensure input isn't too long
            if isinstance(data, str) and len(data) > 5000:
                data = data[:5000] + "\n\n[Input truncated]"

            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": str(data)}
                ],
                temperature=model_config["temperature"],
                max_tokens=model_config["max_tokens"]
            )

            return {
                "success": True,
                "content": completion.choices[0].message.content,
                "model_used": f"{provider}/{model}"
            }

        except Exception as e:
            error_message = str(e).lower()
            logger.warning(f"{provider}/{model} failed: {error_message}")
            st.warning(f"Retrying with backup model... ({tier.value} failed)")

            if "rate limit" in error_message or "quota" in error_message:
                time.sleep(2)

            return self.generate_analysis(data, system_prompt, retry_count + 1)

        return {"success": False, "error": "Unknown failure in model manager"}
