#Part 1
#Possible errors that may occur include:
#Network errors: such as connection timeout or failure to connect to the server.
#Invalid location: the user may input an invalid location or one that the API cannot recognize.
#API errors: the API may not be functioning correctly or may return invalid data.
#To handle these errors, you can use try-except blocks and print informative error messages to the user.

#part 2
#Whether to show local time in Minnesota or UTC time will depend on the purpose of the program and 
#the location of the user. If the program is meant for users in Minnesota or 
#the local time is relevant to the program's functionality, then showing the local time would 
#be appropriate. Otherwise, using UTC time would be a more universal option. 
#It is important to include comments in the program explaining the choice of time format.

#part 3
# This code prompts the user for a location, then fetches the 
# weather forecast for that location using the OpenWeatherMap API.
# It prints the temperature, weather description, and wind speed 
# for every three-hour interval over the next 5 days. The API key is 
# read from an environment variable to avoid hard-coding it into the program. 
# The program also handles errors, and prints an error message if the 
# API request fails.

import os
from pip._vendor import requests
import json
from datetime import datetime

# Read API key from environment variable
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
print(API_KEY)
# User input for location
location = input("Enter location for weather forecast: ")

# Base URL for OpenWeatherMap API
url = 'http://api.openweathermap.org/data/2.5/forecast'

# Query parameters for API request
params = {'q': location, 'appid': API_KEY, 'units': 'metric'}

# Make the API request and get the response
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
   # Parse the JSON data from the response
   data = json.loads(response.text)

   # Extract the forecast information for the next 5 days
   forecast_list = data['list'][:40]

   # Print the forecast information
   for forecast in forecast_list:
       # Convert the timestamp to a human-readable date and time
       date_time = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d %H:%M:%S')

       # Get the temperature and weather description
       temp = forecast['main']['temp']
       description = forecast['weather'][0]['description']

       # Get the wind speed
       wind_speed = forecast['wind']['speed']

       # Print the forecast information for the current time slot
       print(f"At {date_time}, the temperature is {temp:.1f}°C, with {description}, and wind speed of {wind_speed} m/s.")
else:
   # Handle API error
#Part 1
#Possible errors that may occur include:
#Network errors: such as connection timeout or failure to connect to the server.
#Invalid location: the user may input an invalid location or one that the API cannot recognize.
#API errors: the API may not be functioning correctly or may return invalid data.
#To handle these errors, you can use try-except blocks and print informative error messages to the user.

#part 2
#Whether to show local time in Minnesota or UTC time will depend on the purpose of the program and 
#the location of the user. If the program is meant for users in Minnesota or 
#the local time is relevant to the program's functionality, then showing the local time would 
#be appropriate. Otherwise, using UTC time would be a more universal option. 
#It is important to include comments in the program explaining the choice of time format.

#part 3
# This code prompts the user for a location, then fetches the 
# weather forecast for that location using the OpenWeatherMap API.
# It prints the temperature, weather description, and wind speed 
# for every three-hour interval over the next 5 days. The API key is 
# read from an environment variable to avoid hard-coding it into the program. 
# The program also handles errors, and prints an error message if the 
# API request fails.
   from pip._vendor import requests
import os
import json
from datetime import datetime

# Read API key from environment variable
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
print(API_KEY)
# User input for location
location = input("Enter location for weather forecast: ")

# Base URL for OpenWeatherMap API
url = 'http://api.openweathermap.org/data/2.5/forecast'

# Query parameters for API request
params = {'q': location, 'appid': API_KEY, 'units': 'metric'}

# Make the API request and get the response
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
   # Parse the JSON data from the response
   data = json.loads(response.text)

   # Extract the forecast information for the next 5 days
   forecast_list = data['list'][:40]

   # Print the forecast information
   for forecast in forecast_list:
       # Convert the timestamp to a human-readable date and time
       date_time = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d %H:%M:%S')

       # Get the temperature and weather description
       temp = forecast['main']['temp']
       description = forecast['weather'][0]['description']

       # Get the wind speed
       wind_speed = forecast['wind']['speed']

       # Print the forecast information for the current time slot
       print(f"At {date_time}, the temperature is {temp:.1f}°C, with {description}, and wind speed of {wind_speed} m/s.")
else:
   # Handle API error
   print(f"Error fetching weather forecast. Status code: {response.status_code}")