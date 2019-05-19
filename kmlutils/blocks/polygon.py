from __future__ import annotations
from typing import List
from .coordinates import Coordinates
import json


class Polygon:
    """Represents a KML Polygon."""

    def __init__(self):
        """Creates a Polygon object."""
        self._coordinates: List[Coordinates] = []

    def add_coordinate(self, coordinate: Coordinates) -> Polygon:
        """Adds a Coordinate object to the list of the polygon coordinates."""
        if coordinate in self._coordinates:
            raise ValueError('Duplicate coordinate {}.'.format(coordinate.serialize()))

        self._coordinates.append(coordinate)
        return self

    def get_coordinates(self) -> List[Coordinates]:
        """Returns the current polygon's coordinates."""
        return self._coordinates

    def serialize(self) -> str:
        """Returns a JSON representation of the Polygon object"""

        return json.dumps({
            'coordinates': self._coordinates
        })
