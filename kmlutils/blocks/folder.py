from __future__ import annotations
from .placemark import PlaceMark
from .element import Element
from typing import List
import json


class Folder(Element):
    """Represents a KML folder."""

    def __init__(self):
        """Creates a new KML folder object."""

        super(Folder, self).__init__()
        self._placemarks: List[PlaceMark] = []

    def add_placemark(self, placemark: PlaceMark) -> Folder:
        """Adds a PlaceMark to the folder."""
        if placemark in self._placemarks:
            raise ValueError('Duplicate PlaceMark {}.'.format(placemark.serialize()))

        self._placemarks.append(placemark)
        return self

    def serialize(self) -> str:
        """Returns a JSON representation of the Folder."""
        return json.dumps({
            'name': self._name,
            'description': self._description,
            'placemarks': self._placemarks
        })
