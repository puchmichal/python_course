from .weather import Weather


class WeatherFormatter:
    _LINE_LEN = 45
    _APP_TITLE = "WEATHER CHECK ☀"

    def __init__(self, weather: Weather):
        self.weather = weather

    def format(self) -> str:
        """Returns data from weather object formatted."""
        formatted_results = "=" * self._LINE_LEN + "\n"
        formatted_results += self._APP_TITLE + "\n\n"

        formatted_results += f"Current weather in {self.weather.city}:\n"
        formatted_results += f"\tWeather type: {self.weather.weather_type}\n"
        formatted_results += f"\tTemperature: {self.weather.temperature}\n"
        formatted_results += f"\tFeels like: {self.weather.feels_like}\n"
        formatted_results += f"\tHumidity: {self.weather.humidity}\n"
        formatted_results += "=" * self._LINE_LEN

        return formatted_results
