from flask import jsonify
from utils import *
import pandas as pd

# This is a header that needs to be in all responses going to a browser or else it breaks
base_header = {'Access-Control-Allow-Origin': '*'}

def handle_preflight_request():
    ''' Gives the necessary response to a confirmation request that the browser will send before the actual response. '''
    headers = base_header.copy()
    headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return ('', 204, headers)


def handle_post_request(request):  

    # Check to make sure all of the keys are correct or return a failed response
    missing_keys = [] 
    for expected_key in ['prompt', 'month', 'crowdPreference']:
        if expected_key not in request.json.keys():
            missing_keys.append(expected_key)
    if missing_keys:
        message = {'message': f'Missing the following keys: {",".join(missing_keys)}'}
        return (jsonify(message), 404, base_header)

    # Pull out the request elements into variables
    prompt = request.json['prompt']
    month = request.json['month']
    crowdPreference = request.json['crowdPreference']

    message = {
        'message': 'success',
        'data': f'The prompt is {prompt}. The month is {month}. The crowdPreference is {crowdPreference}.'
    } 
    return (jsonify(message), 200, base_header)
################################################  THIS SECTION ADDED BY IAN  ############################################
# Load data to be used by Drop Down Options for Enter City + Calculating Parks distances from city
def load_and_initialize_data():
    """Load CSV files and initialize data globally."""
    try:
        # Load the CSV files
        cities_df = pd.read_csv(CITY_CSV_PATH) # Add path for world_cities.csv
        parks_df = pd.read_csv(PARK_CSV_PATH) # Add path for most updated parks.csv

        # Store the data globally
        app.config['CITIES_DF'] = cities_df
        app.config['PARKS_DF'] = parks_df
        app.config['CITIES_LIST'] = cities_df['City_Country'].unique().tolist()  # Store city list for drop down options

        print("Data loaded successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        app.config['CITIES_DF'] = None
        app.config['PARKS_DF'] = None
        app.config['CITIES_LIST'] = []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        app.config['CITIES_DF'] = None
        app.config['PARKS_DF'] = None
        app.config['CITIES_LIST'] = []

# Call load_and_initialize_data() at startup
load_and_initialize_data()
#########################################################################################################################
################################################# Added by Ian ##########################################################
# To handle request by dropdown to get list of cities
def get_cities():
    """Handle city search requests via AJAX."""
    query = request.args.get('query', '')
    if not query:
        return jsonify({"message": "No query parameter provided"}), 400

    # Get the city list from app.config
    matching_cities = [city for city in app.config['CITIES_LIST'] if city.lower().startswith(query.lower())]
    matching_cities.sort()
    return jsonify(matching_cities)
##########################################################################################################################
def main(request):
  
    if request.method == 'OPTIONS':
        return handle_preflight_request()

    elif request.method == 'GET':
        return (jsonify({'message': 'success'}), 200, base_header)

    elif request.method == 'POST':
        return handle_post_request(request)

    else:
        headers = {'Access-Control-Allow-Origin': '*'}
        message = {'message': 'unsupported method'}
        return (jsonify(message), 404, headers)
