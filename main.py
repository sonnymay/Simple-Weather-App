import requests

API_KEY = "c8fbc8a4da6f4d2376db9c4c7e5d3c99"

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&cnt=4"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None


def display_weather_data(city, weather_data):
    if weather_data is not None:
        print(f"Weather forecast for {city}:\n")
        
        for entry in weather_data["list"]:
            dt_txt = entry["dt_txt"]
            temp = entry["main"]["temp"]
            description = entry["weather"][0]["description"]
            
            print(f"{dt_txt}: {temp:.1f}°C, {description}")


def main():
    while True:
        city = input("\nEnter the name of a city (or 'exit' to quit): ")
        
        if city.lower() == "exit":
            break
        
        weather_data = get_weather_data(city)
        display_weather_data(city, weather_data)


if __name__ == "__main__":
    main()
