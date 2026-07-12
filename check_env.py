from dotenv import load_dotenv
import os

load_dotenv()

print("URL:", os.getenv("IBM_URL"))
print("PROJECT_ID:", os.getenv("IBM_PROJECT_ID"))
print("API KEY EXISTS:", bool(os.getenv("IBM_API_KEY")))