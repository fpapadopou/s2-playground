from __future__ import annotations
from typing import List
from .folder import Folder
from .element import Element
import json


class Document(Element):
    """Represents a KML Document."""

    def __init__(self):
        """Creates a new KML document."""

        super(Document, self).__init__()
        self._folders: List[Folder] = []

    def add_folder(self, folder: Folder) -> Document:
        """Adds a folder to the current document."""
        if folder in self._folders:
            raise ValueError('Duplicate folder {}.'.format(folder.serialize()))

        self._folders.append(folder)
        return self

    def serialize(self) -> str:
        """Returns a JSON representation of the KML document."""
        return json.dumps({
            'name': self._name,
            'description': self._description,
            'folders': self._folders
        })
