
import requests

API_KEY = input("Enter your API key: ")

def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        print("API Status Code:", response.status_code)

        response.raise_for_status()

        data = response.json()

        print("\n===== WEATHER REPORT =====")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])

        forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

        forecast_response = requests.get(
            forecast_url, params=params, timeout=10
        )

        forecast_response.raise_for_status()
        forecast = forecast_response.json()

        print("\n===== SHORT FORECAST =====")

        for item in forecast["list"][:3]:
            print(item["dt_txt"], "-", item["weather"][0]["description"])

    except requests.exceptions.HTTPError:
        print("API Error:", response.status_code)
        print(response.text)

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)


city = input("Enter city name: ")
get_weather(city)

