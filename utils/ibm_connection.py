import os
from dotenv import load_dotenv
import streamlit as st

from ibm_watsonx_ai import Credentials, APIClient
from ibm_watsonx_ai.foundation_models import ModelInference

# Load environment variables from .env (for local development)
load_dotenv()


def get_secret(key):
    """
    Get configuration from:
    1. Render Environment Variables / .env
    2. Streamlit secrets (if available)
    """
    value = os.getenv(key)
    if value:
        return value

    try:
        return st.secrets[key]
    except Exception:
        raise ValueError(f"Missing configuration: {key}")


IBM_URL = get_secret("IBM_URL")
IBM_API_KEY = get_secret("IBM_API_KEY")
IBM_PROJECT_ID = get_secret("IBM_PROJECT_ID")


credentials = Credentials(
    url=IBM_URL,
    api_key=IBM_API_KEY
)

client = APIClient(credentials)
client.set.default_project(IBM_PROJECT_ID)

model = ModelInference(
    model_id="meta-llama/llama-3-3-70b-instruct",
    api_client=client,
    params={
        "max_new_tokens": 300,
        "temperature": 0.7
    }
)


def ask_llama(prompt):
    response = model.generate_text(prompt=prompt)
    return response