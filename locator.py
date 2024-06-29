from functools import partial
from typing import Self
from enum import Enum


class Attribute:
    """Locator attribute of format <key>:<value>"""

    class AttrKey(Enum):
        ID = "id"
        TYPE = "type"
        CLASS = "class"
        NAME = "name"

    def __init__(self, key: AttrKey, value: str):
        self.key: str = key.value
        self.value: str = f'"{value}"' if " " in value else value

    @classmethod
    def _id(cls, id_val: str):
        return cls(Attribute.AttrKey.ID, id_val)

    @classmethod
    def _name(cls, name_val: str) -> Self:
        return cls(Attribute.AttrKey.NAME, name_val)

    @classmethod
    def _type(cls, type_val: str) -> Self:
        return cls(Attribute.AttrKey.TYPE, type_val)

    @classmethod
    def _class(cls, class_val: str) -> Self:
        return cls(Attribute.AttrKey.CLASS, class_val)

    def __str__(self) -> str:
        return f"{self.key}:{self.value}"


# Attribute shortcuts
BUTTON = Attribute._type(type_val="button")
TEXT = Attribute._type(type_val="text")
COMBO = Attribute._type(type_val="combobox")
LIST_ITEM = Attribute._type(type_val="listItem")

ID = Attribute._id
TYPE = Attribute._type
CLASS = Attribute._class
NAME = Attribute._name


def make_elem(*attrs) -> str:
    return " ".join([f"{attr.key}:{attr.value}" for attr in attrs])


def make_tree(*elems) -> str:
    return " > ".join(str(elem) for elem in elems)
