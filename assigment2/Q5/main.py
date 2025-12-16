
from dotenv import load_dotenv
import os
from utlis import get_weather

load_dotenv()  # loads .env file

def main():
    city = input("Enter city name: ")
    data = get_weather(city)
    print(f"Full Data : \n {data}")
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print("\n--- Weather Report ---")
    print(f"Temperature: {temp} °C")
    print(f"Humidity: {humidity} %")

if __name__ == "__main__":
    main()