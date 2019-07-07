from __future__ import annotations
from typing import List
from .point import Point
import json


class Polygon:
    """Represents a KML Polygon."""

    def __init__(self):
        """Creates a Polygon object."""
        self._coordinates: List[Point] = []

    def add_point(self, point: Point) -> Polygon:
        """Adds a Point object to the list of the polygon coordinates."""
        if point in self._coordinates:
            raise ValueError('Duplicate point {} in polygon coordinates.'.format(point.serialize()))

        self._coordinates.append(point)
        return self

    def get_coordinates(self) -> List[Point]:
        """Returns the current polygon's coordinates."""
        return self._coordinates

    def serialize(self) -> str:
        """Returns a JSON representation of the Polygon object"""

        return json.dumps({
            'coordinates': self._coordinates
        })
