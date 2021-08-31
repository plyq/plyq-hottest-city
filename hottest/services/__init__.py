import hottest.service as hs
import hottest.services.open_weather as hsow

AVAILABLE_SERVICES = [
    "open_weather",
]


def from_string(name: str) -> hs.WeatherService:
    if name not in AVAILABLE_SERVICES:
        raise ValueError("Service does not exist: %s" % name)
    if name == "open_weather":
        return hsow.OpenWeatherService()
    else:
        raise NotImplementedError("Service does not implemented: %s" % name)
