"""API get func."""

import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = 'https://api.weather.yandex.ru/v2/informers?lat={}&lon={}'
OK = 200

KEY = os.environ.get('KEY')
EXIT_MSG = os.environ.get('EXIT_MSG')

headers = {'X-Yandex-API-Key': KEY}


def get_weather_by_city(coordinates: tuple[float]) -> dict:
    """Func that makes an API request towards YANDEX-WEATHER-API.

    Args:
        coordinates (tuple[float]): coords of the place we are requesting weather.

    Returns:
        dict: edited response from YWA
    """
    response = requests.get(URL.format(*coordinates), headers=headers)
    if response.status_code == OK:
        weather = json.loads(response.content)
        forecast = weather
        forecast.pop('now')
        forecast.pop('info')
        forecast.pop('fact')
    
        forecast.pop('now_dt')

        return forecast
