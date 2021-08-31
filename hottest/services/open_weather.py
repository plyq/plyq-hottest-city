import gzip
import io
import json
from typing import Dict, Optional

import aiohttp
import requests

import hottest.config as hcfg
import hottest.service as hs


class OpenWeatherService(hs.WeatherService):
    BASE_URL = "http://api.openweathermap.org/data/2.5"
    CITIES_URL = (
        "http://bulk.openweathermap.org/sample/current.city.list.json.gz"
    )

    def __init__(self):
        self._api_token = None
        self._cities = None

    async def get_weather(self, city: str) -> float:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.BASE_URL + "/weather",
                params={
                    "id": city,
                    "units": "metric",
                    "APPID": self.api_token,
                },
            ) as response:
                weather = await response.json()
        try:
            return weather["main"]["temp"]
        except KeyError:
            raise ConnectionError(weather["message"])

    async def get_city_id(self, city: str) -> Optional[str]:
        try:
            return self.cities[city]
        except KeyError:
            return None

    @property
    def cities(self) -> Dict[str, str]:
        if self._cities is not None:
            return self._cities
        # Get cities from web.
        res = requests.get(self.CITIES_URL, timeout=30, stream=True)
        json_gz_content = res.content
        virtual_file = io.BytesIO(json_gz_content)
        with gzip.GzipFile(fileobj=virtual_file) as fh:
            data = json.loads(fh.read(), encoding="utf-8")
        self._cities = {item["name"]: str(item["id"]) for item in data}
        return self._cities

    @property
    def api_token(self) -> str:
        if self._api_token is not None:
            return self._api_token
        self._api_token = hcfg.get("OPENWEATHER_TOKEN")
        return self._api_token
