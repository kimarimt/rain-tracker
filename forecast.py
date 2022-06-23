from dotenv import load_dotenv
from dataclasses import dataclass
from datetime import datetime
import os
import requests

load_dotenv()
OPEN_WEATHER_API = os.getenv('OPEN_WEATHER_API')
MY_LOCATION = (42.628170, -83.329010)


@dataclass
class Forecast:
    time: str
    weather: str


def get_hourly_forecast():
    params = {
        'lat': MY_LOCATION[0],
        'lon': MY_LOCATION[1],
        'exclude': 'current,minutely,daily,alerts',
        'appid': OPEN_WEATHER_API,
    }
    response = requests.get(
        url='https://api.openweathermap.org/data/3.0/onecall',
        params=params
    )
    response.raise_for_status()

    forecasts = []

    for entry in response.json()['hourly'][:12]:
        forecast = Forecast(
            time=datetime.fromtimestamp(entry['dt']).strftime('%I:%M %p'),
            weather=entry['weather'][0]['main'],
        )
        forecasts.append(forecast)

    return forecasts
