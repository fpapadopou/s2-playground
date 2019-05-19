import json


class Coordinates:
    """Represents a lat-lng pair."""

    def __init__(self, lat: float, lng: float):
        """Create a Coordinates object."""

        self._validate_coords(lat, lng)

        self._lat = lat
        self._lng = lng

    def get_lat(self) -> float:
        """Latitude getter."""
        return self._lat

    def get_lng(self) -> float:
        """Longitude getter."""
        return self._lng

    def serialize(self) -> str:
        """Returns a JSON representation of the object."""
        return json.dumps({'lat': self._lat, 'lng': self._lng})

    def _validate_coords(self, lat, lng) -> None:
        """Validates coordinates input."""

        if lat is None or lng is None:
            raise ValueError('Latitude & longitude cannot be empty.')

        if lat > 90.0 or lat < -90.0:
            raise ValueError('Latitude must be between -90 & 90.')

        if lng > 180.0 or lng < -180.0:
            raise ValueError('Longitude must be between -180 & 180.')
