# Weather check app
CLI app to check current weather.

## Installation

To install the app run while being in root folder(/project):
```shell
pip install .
```

App requires WEATHER_APP_ID enviromental variable. APP_ID from https://openweathermap.org/ should be set to this variable.
This step is nessecarry to use app.

## Usage

To check weather in Warsaw run:
```shell
weather-app
```

If you want to check weather in different city run for example:
```shell
weather-app -c Krakow
```

If you want to check weather in different city that's not in Poland run for example:
```shell
weather-app -c "New York" --country US
```

For detailed help run"
```shell
weather-app --help
```