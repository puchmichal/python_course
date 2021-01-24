import os

import requests
from requests.models import Response


class RequestHandler:
    """Resposible for creating and sending GET request to openweathermap API."""

    _CURRENT_WEATHER_REQUEST_TYPE = "weather"
    _REQUEST_TEMPLATE = (
        "http://api.openweathermap.org/data/2.5/{request_type}?q={city},{country}&APPID={app_id}"
    )

    def __init__(self, city: str, country: str):
        self.city = city
        self.country = country

        if os.getenv("WEATHER_APP_ID") and os.getenv("WEATHER_APP_ID") != "0":
            self._app_key = os.getenv("WEATHER_APP_ID")
        else:
            raise RuntimeError("Environmental variable WEATHER_APP_ID not found.")

    def get_json_results(self) -> dict:
        """Returns Response form openweathermap API.

        Raises:
            ValueError: when response code is not equal to 200

        Returns:
            dict, json response
        """
        response = self._send_request().json()
        if response["cod"] != 200:
            raise ValueError("Incorrect city or country.")
        return response

    def _send_request(self) -> Response:
        return requests.get(self._create_url())

    def _create_url(self) -> str:
        request_type = self._CURRENT_WEATHER_REQUEST_TYPE

        return self._REQUEST_TEMPLATE.format(
            city=self.city, country=self.country, app_id=self._app_key, request_type=request_type
        )
