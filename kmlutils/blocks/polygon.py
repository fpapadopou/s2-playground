from __future__ import annotations
from typing import List
from .point import Point
from shapely.geometry import Polygon as ShapelyPolygon
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

    def validate(self):
        """Validates the current polygon's coordinate list."""
        polygon = ShapelyPolygon(self._coordinates)
        if not polygon.is_valid():
            raise ValueError('Invalid Polygon coordinates: {}'.format(self.serialize()))

    def serialize(self) -> str:
        """Returns a JSON representation of the Polygon object"""

        return json.dumps({
            'coordinates': self._coordinates
        })
