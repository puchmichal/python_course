import argparse

from .weather_check_app import WeatherCheckApp


def main(args=None):
    # parse arguments
    parser = argparse.ArgumentParser(
        prog="weather-check",
        description="CLI OpenWeather API clinet.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-c", "--city", type=str, default="Warsaw", help="Name of the city.")
    parser.add_argument("--country", type=str, default="pl", help="ISO code of country.")

    args = parser.parse_args(args)

    # run WeatherCheckApp
    weather_check_app = WeatherCheckApp(args=args)
    weather_check_app.run()
