import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
print(API_KEY)
URL = 'https://api.api-ninjas.com/v1/animals?'

def fetch_data(animal_name):
    headers = {'X-Api-Key': API_KEY}
    params = {'name': animal_name}

    try:
      # Send the GET request
      response = requests.get(URL, headers=headers, params=params)

      # Print status and raw content to find the root cause
      print(f"Status Code: {response.status_code}")
      print(f"Raw Response: {response.text}")

      # Only parse if status is successful
      if response.status_code == 200:
          animals_data = response.json()
          print(animals_data)
          return animals_data
      else:
          print("Request failed. Check the raw response above for details.")

    except requests.exceptions.RequestException as e:
      print(f"An error occurred: {e}")