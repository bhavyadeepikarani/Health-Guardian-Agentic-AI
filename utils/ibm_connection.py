import streamlit as st

from ibm_watsonx_ai import Credentials, APIClient
from ibm_watsonx_ai.foundation_models import ModelInference


# Load IBM Watsonx credentials from Streamlit Secrets
credentials = Credentials(
    url=st.secrets["IBM_URL"],
    api_key=st.secrets["IBM_API_KEY"]
)

# Get IBM Watsonx project ID
project_id = st.secrets["IBM_PROJECT_ID"]


# Create API client
client = APIClient(credentials)

# Set default project
client.set.default_project(project_id)


# Create Watsonx model
model = ModelInference(
    model_id="meta-llama/llama-3-3-70b-instruct",
    api_client=client,
    params={
        "max_new_tokens": 300,
        "temperature": 0.7
    }
)


def ask_llama(prompt):
    """
    Send prompt to IBM Watsonx Llama model
    """

    response = model.generate_text(
        prompt=prompt
    )

    return response