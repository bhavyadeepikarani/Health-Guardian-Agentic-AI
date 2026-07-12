from dotenv import load_dotenv
import os

from ibm_watsonx_ai import Credentials, APIClient
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

credentials = Credentials(
    url=os.getenv("IBM_URL"),
    api_key=os.getenv("IBM_API_KEY")
)

project_id = os.getenv("IBM_PROJECT_ID")

# Create API client first
client = APIClient(credentials)
client.set.default_project(project_id)

# Create model
model = ModelInference(
    model_id="meta-llama/llama-3-3-70b-instruct",
    api_client=client,
    params={
        "max_new_tokens": 300,
        "temperature": 0.7
    }
)

def ask_llama(prompt):
    return model.generate_text(prompt=prompt)