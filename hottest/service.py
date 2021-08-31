import abc


class WeatherService(abc.ABC):
    @abc.abstractmethod
    async def get_weather(self, city: str) -> float:
        pass

    @abc.abstractmethod
    async def get_city_id(self, city: str) -> str:
        pass
