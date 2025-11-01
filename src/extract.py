import requests
import json
import pandas as pd
from src.config import BASE_URL, API_KEY

# add city name and state code to the list
# The index of each city must match the index of its state
cities = ["San Antonio"]
states = ["TX"]

def extract_properties(city, state):
    headers = {
        "accept": "application/json",
        "X-Api-Key": API_KEY
        }
    params = {
        "city": city, 
        "state": state
        }
    print(f"fetching properties data for {city} and {state}")
    response = requests.get(BASE_URL, headers = headers, params = params)
    
    if response.status_code == 200:
        data = response.json()
    
    else:
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        
for city, state in zip(cities, states):
     data = extract_properties(city, state)  

file_name =  f"data/raw/{city}_{state}_properties_data_.json"

with open(file_name, "w") as f:
    json.dump(data, f, indent = 2)