from __future__ import annotations


class Element:
    """Represents a KML element with a name and description."""

    def __init__(self):
        """Creates a new Element object with an empty name & description."""
        self._name: str = ''
        self._description: str = ''

    def set_name(self, name: str) -> Element:
        """Element name setter."""
        self._name = name

        return self

    def set_description(self, description: str) -> Element:
        """Element description getter."""
        self._description = description

        return self
