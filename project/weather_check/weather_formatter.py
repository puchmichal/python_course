import os

from .weather import Weather


class WeatherFormatter:
    _LINE_LEN = 45
    _APP_TITLE = "WEATHER CHECK"

    def __init__(self, weather: Weather):
        self.weather = weather

    def format(self) -> str:
        """Returns data from weather object formatted."""
        formatted_results = "=" * self._LINE_LEN + f"{os.linesep}"
        formatted_results += self._APP_TITLE + f"{os.linesep}" * 2

        formatted_results += f"Current weather in {self.weather.city}:{os.linesep}"
        formatted_results += f"\tWeather type: {self.weather.weather_type}{os.linesep}"
        formatted_results += f"\tTemperature: {self.weather.temperature}{os.linesep}"
        formatted_results += f"\tFeels like: {self.weather.feels_like}{os.linesep}"
        formatted_results += f"\tHumidity: {self.weather.humidity}{os.linesep}"
        formatted_results += "=" * self._LINE_LEN

        return formatted_results
