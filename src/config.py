import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from a .env file into environment

BASE_URL = "https://api.rentcast.io/v1/properties"

API_KEY = os.getenv("RENTCAST_API_KEY")  # Fetches the API key

