import os
import requests

def get_weather(city):
   apikey=os.getenv("apikey")

   url=f"https://api.openweathermap.org/data/2.5/weather?appid={apikey}&q={city}&units=metric"

   response=requests.get(url)
   return response.json()