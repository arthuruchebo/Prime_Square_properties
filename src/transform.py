import json
import pandas as pd

file_path = "/Users/arthuruchebo_Pro/Documents/Projects/Amdari/amdari_DE/Prime_Square_Properties/data/raw/San Antonio_TX_properties_data"

def transform(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    print(len(data))
    df = pd.json_normalize(data)
    
    columns = [
        'id', 'formattedAddress', 'addressLine1', 'addressLine2', 'city','state', 'stateFips', 'zipCode', 'county',
        'countyFips', 'latitude', 'longitude', 'propertyType', 'bedrooms', 'bathrooms', 'squareFootage', 'yearBuilt'
        ]
    
    df = df[columns]

    df.rename( columns = {'formattedAddress' : 'address', 
                        'stateFips': 'state_fips', 
                        'zipCode' : 'zip_code',
                        'countyFips' : 'county_fips',
                        'propertyType': 'property_type',
                        'squareFootage': 'square_footage', 
                        'yearBuilt': 'year_built'
                        }, inplace = True)
    
    data = "data/transformed/San Antonio_TX_properties_data.csv"
    
    df.to_csv(data, index = True)
    return data