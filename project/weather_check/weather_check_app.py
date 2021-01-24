from argparse import Namespace

from .request_handler import RequestHandler
from .weather import Weather
from .weather_formatter import WeatherFormatter


class WeatherCheckApp:
    """Weather-check runner. Sends request and prints formatted results"""

    def __init__(self, args: Namespace):
        self.args = args

    def run(self) -> None:
        """Prints formatted results."""
        request_handler = RequestHandler(city=self.args.city, country=self.args.country)
        json = request_handler.get_json_results()

        weather = Weather(json=json)

        weather_formatter = WeatherFormatter(weather=weather)
        print(weather_formatter.format())
