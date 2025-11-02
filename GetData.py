import requests

geocodeUrl = "https://api.openweathermap.org/geo/1.0/direct"
weatherUrl = "https://api.open-meteo.com/v1/forecast"

APIKey = "c972816654fbe292c7069105e83e98f7"


def getCoordinates(city):
    params = {
        "appid": APIKey,
        "q": city,
        "limit": 1
    }
    response = requests.get(url=geocodeUrl, params=params)
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code}")

    data = response.json()


    if not data or not isinstance(data, list):
        raise ValueError("No valid data returned")

    lat = data[0].get("lat")
    lon = data[0].get("lon")

    if lat is None or lon is None:
        raise ValueError("Incomplete data received from API.")

    return lat, lon

def getWeather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,relative_humidity_2m"
    }

    response = requests.get(url=weatherUrl, params=params)
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code}")
    data = response.json()
    weather = {
        "temperature": data["current"]["temperature_2m"],
        "wind_speed": data["current"]["wind_speed_10m"],
        "relative_humidity": data["current"]["relative_humidity_2m"]
    }
    return weather

def getWeatherReport(city):
    try:
        lat, lon = getCoordinates(city)
        weather = getWeather(lat, lon)
        report = {
            "city": city,
            "temperature": weather["temperature"],
            "wind_speed": weather["wind_speed"],
            "relative_humidity": weather["relative_humidity"]
        }
        return report
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
   print(getWeatherReport(input("Enter city name: ")))
