import requests
import time


class WeatherAPIError(Exception):
    """Custom exception for weather API errors."""
    pass


class WeatherAPIClient:

    def __init__(self):
        self.geo_url = (
            "https://geocoding-api.open-meteo.com/v1/search"
        )

        self.weather_url = (
            "https://api.open-meteo.com/v1/forecast"
        )

    def request_with_retry(
        self,
        url,
        params,
        retries=3
    ):
        for attempt in range(retries):

            try:
                response = requests.get(
                    url,
                    params=params,
                    timeout=10
                )

                response.raise_for_status()

                return response.json()

            except requests.RequestException:

                if attempt == retries - 1:
                    raise WeatherAPIError(
                        "Request failed after retries."
                    )

                time.sleep(2 ** attempt)

    def geocode_location(
        self,
        location
    ):

        data = self.request_with_retry(
            self.geo_url,
            {
                "name": location,
                "count": 1
            }
        )

        result = data["results"][0]

        return (
            result["latitude"],
            result["longitude"]
        )

    def get_forecast(
        self,
        latitude,
        longitude
    ):

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_sum"
            ],
            "timezone": "auto"
        }

        return self.request_with_retry(
            self.weather_url,
            params
        )