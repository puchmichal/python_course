class Weather:
    """Weather details object based on request."""

    @property
    def temperature(self) -> str:
        """Returns temperatur in c."""
        temperature_in_kelvins = self.json["main"]["temp"]
        return self._get_formatted_c(temperature_in_kelvins)

    @property
    def feels_like(self) -> str:
        """Returns feel like temperature in c."""
        feels_like_in_kelvins = self.json["main"]["feels_like"]
        return self._get_formatted_c(feels_like_in_kelvins)

    @property
    def humidity(self) -> float:
        """Return humidity level."""
        humidity = self.json["main"]["humidity"]
        return humidity / 100

    @property
    def weather_type(self) -> float:
        """Returns weather type"""
        return self.json["weather"][0]["main"]

    @property
    def city(self) -> str:
        """Returns city name"""
        return self.json["name"]

    def __init__(self, json: dict):
        self.json = json

    def _get_formatted_c(self, k: float) -> str:
        """Formats temperature expressed in kelvins to celcius.

        Args:
            k: float, temperature in kelvins

        Returns:
            string, formatted temperature in celcius
        """
        return format(self._k_to_c(k), ".1f")

    @staticmethod
    def _k_to_c(k: float) -> float:
        """Transform temperature expressed in kelvins to celcius

        Args:
            k: float, temperature in kelvins

        Returns:
            float, temperature in celcius
        """
        return k - 273.15
