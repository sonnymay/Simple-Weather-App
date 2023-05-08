import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('OPENWEATHER_API_KEY')

def get_weather_data(location):
    # Check if the location is a digit, if so assume it's a zip code
    if location.isdigit():
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={location},us&appid={API_KEY}&units=metric"
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None

def display_weather_data(weather_data):
    city = f"{weather_data['name']}, {weather_data['sys']['country']}"
    temp_celsius = weather_data['main']['temp']
    temp_fahrenheit = (temp_celsius * 1.8) + 32
    feels_like_celsius = weather_data['main']['feels_like']
    feels_like_fahrenheit = (feels_like_celsius * 1.8) + 32
    description = weather_data['weather'][0]['description']

    print(f"\nWeather forecast for {city}:")
    print(f"Temperature: {temp_celsius:.1f}°C ({temp_fahrenheit:.1f}°F)")
    print(f"Feels like: {feels_like_celsius:.1f}°C ({feels_like_fahrenheit:.1f}°F)")
    print(f"Description: {description}")

def main():
    while True:
        location = input("\nEnter a city name or zip code (or 'exit' to quit): ")
        
        if location.lower() == "exit":
            break
        
        weather_data = get_weather_data(location)
        
        if weather_data is not None:
            display_weather_data(weather_data)


if __name__ == "__main__":
    main()