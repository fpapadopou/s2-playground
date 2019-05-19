from .polygon import Polygon
from .element import Element
import json


class PlaceMark(Element):
    """Represents a KML placemark."""

    def __init__(self):
        """Creates a new PlaceMark object."""

        super(PlaceMark, self).__init__()
        self._polygon: Polygon = None

    def serialize(self) -> str:
        """Returns a JSON """
        return json.dumps({
            'name': self._name,
            'description': self._description,
            'polygon': self._polygon
        })
