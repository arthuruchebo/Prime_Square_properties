from extract import extract_properties
from transform import transform
from load import load_to_db

def run_pipeline():
    print("starting pipeline run")
    
    raw_file = extract_properties(city= 'San Antonio', state= 'TX')
    if raw_file:
        clean_file = transform(raw_file)
        load_to_db(clean_file)
        print('ETL pipeline successful')
    else:
        print('ETL pipeline not successful')
        
if __name__ == "__main__":
    run_pipeline()
    