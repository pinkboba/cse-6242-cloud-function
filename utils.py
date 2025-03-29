# In this file, we can write individual python functions to be used in the main file

# I sketched out a few of the functions that I think would be necessary and what I think the inputs and outputs would look like.
# This is can all be changed and adjusted according to everyone's thoughts

def recommend_parks(prompt: str, month: int, crowdPreference: int):
  """ The main function that takes in the user's input and returns a list of dictionaries, sorted from highest to lowest recommendation score. """
  pass

def calculate_prompt_review_similarity_scores(prompt: str):
  """ Given a prompt, calculate the prompt's similarity to the google reviews and return the score for each park as a list of dictionaries. """
  pass

def calculate_prompt_wikipedia_similarity_scores(prompt: str):
  """ Given a prompt, calculate the prompt's similarity to the Wikipedia pages and return the score for each park as a list of dictionaries. """
  pass

def calculate_crowd_scores(month: int, crowdPreference: int):
  """ Given a month as a number 1-12 and a crowdPreference value 0 or 1, look up the park-specific crowd index for each park for the given month. """
  pass

def calculate_distance_to_parks(city_name: str):
  """ Given a city name, returns a list of dictionaries with the distance from that city to each park. """
  pass
  
