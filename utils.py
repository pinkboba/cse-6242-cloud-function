# Imports
import pandas as pd
from geopy.distance import geodesic # Required for def calculate_distance_to_parks

# In this file, we can write individual python functions to be used in the main file

# I sketched out a few of the functions that I think would be necessary and what I think the inputs and outputs would look like.
# This is can all be changed and adjusted according to everyone's thoughts

def recommend_parks(prompt: str, month: int, crowdPreference: int):
  """ The main function that takes in the user's input and returns a dataframe, sorted from highest to lowest recommendation score. """
  pass

def calculate_prompt_review_similarity_scores(prompt: str):
  """ Given a prompt, calculate the prompt's similarity to the google reviews and return the score for each park as a dataframe. """
  pass

def calculate_prompt_wikipedia_similarity_scores(prompt: str):
  """ Given a prompt, calculate the prompt's similarity to the Wikipedia pages and return the score for each park as a dataframe. """
  pass

def calculate_crowd_scores(month: int, crowdPreference: int):
  """ Given a month as a number 1-12 and a crowdPreference value 0 or 1, look up the park-specific crowd index for each park for the given month. """
  pass

def calculate_distance_to_parks(city_name: str): #(city_name: str, cities_df, parks_df): Switch if inputs for cities_df, parks_df exist
  """
  Takes city_name and calculates distance in miles to all parks (62 - Kings and Sequoia National Park both under 'seki' park code, so distance will be the same).
  Returns dataframe 62 x 3 columns - Park Name, Park Code, Distance_miles
  Code assumes no inputs for parks_df, cities_df. Code will load csv files from a local file path.
  If 
  """
  # Include if assuming csv not loaded globally
  cities_df = pd.read_csv("../worldcities_data.csv") # Change CSV file path as required
  parks_df = pd.read_csv("../parks_03132025.csv") # Change CSV file path as required

  # Ensure city_name is in cities_csv or cities_df
  try:
    city = cities_df[cities_df["City_Country"] == city_name]  # Sub cities_csv for cities_df if required
  except:
    raise ValueError(f"{city_name} not found in the cities list.")

  # Get city coordinates
  city_lat, city_lon = city.iloc[0]['lat'], city.iloc[0]['lng']

  # Calculate distances from city to each park
  distances = []
  for _, row in parks_df.iterrows():
      park_lat, park_lon = row['Latitude'], row['Longitude']
      distance_miles = geodesic((city_lat, city_lon), (park_lat, park_lon)).miles
      distances.append({'Park Name': row['Park Name'], 'Park Code': row['Park Code'], 'Distance_miles': round(distance_miles, 2)})

  # Convert list of distances to DataFrame
  distances_df = pd.DataFrame(distances)

  # Sort distances in ascending order
  distances_df = distances_df.sort_values(by='Distance_miles', ascending=True)

  # Return dataframe
  return distances_df # returns dataframe of shape 62 x 3 (columns = Park Name, Park Code, Distance_miles). 62 total rows (not 63) as in NPS data Kings and Sequoia National Park are consider one and labeled as 'seki' Park Code.
  
