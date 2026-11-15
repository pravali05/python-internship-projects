
import requests
from getpass import getpass

API_KEY = getpass("Enter your OpenWeather API key: ")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("\n----- WEATHER REPORT -----")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])

        forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
        forecast_response = requests.get(
            forecast_url,
            params=params,
            timeout=10
        )
        forecast_response.raise_for_status()

        forecast = forecast_response.json()

        print("\n----- SHORT FORECAST -----")
        for item in forecast["list"][:3]:
            print(
                item["dt_txt"],
                "-",
                item["weather"][0]["description"]
            )

    except requests.exceptions.HTTPError:
        print("Invalid city or API key. Please check again.")
    except requests.exceptions.RequestException:
        print("Network error. Please try again.")

city = input("Enter city name: ")
get_weather(city)
