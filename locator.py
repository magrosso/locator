from typing import Self
from functools import partialmethod
from enum import Enum


class AttrKey(Enum):
    ID = "id"
    TYPE = "type"
    CLASS = "class"
    NAME = "name"


class Attribute:
    """Locator attribute of format <key>:<value>"""

    def __init__(self, key: AttrKey, value: str):
        self.key = key.value
        self.value = f'"{value}"' if " " in value else value

    @classmethod
    def from_id(cls, id_val: str):
        return cls(AttrKey.ID, id_val)

    @classmethod
    def from_name(cls, name_val: str):
        return cls(AttrKey.NAME, name_val)

    @classmethod
    def from_type(cls, type_val: str):
        return cls(AttrKey.TYPE, type_val)

    @classmethod
    def from_class(cls, class_val: str):
        return cls(AttrKey.CLASS, class_val)

    button = partialmethod(from_type, type_val="button")
    text = partialmethod(from_type, type_val="text")
    combo = partialmethod(from_type, type_val="combobox")
    list_item = partialmethod(from_type, type_val="listItem")

    def __str__(self) -> str:
        return f"{self.key}:{self.value}"


BUTTON = Attribute.button()
TEXT = Attribute.text()
COMBO = Attribute.combo()
LIST = Attribute.list_item()


class Element:
    """Create an Element object from one or more Attributes.
    An Element is a space-separated list of Attributes identifying a single UI element"""

    def __init__(self, *attrs: Attribute):
        self.attrs: list[Attribute] = list(attrs)
        self.elem: str = self.from_attr()

    def from_attr(self) -> str:
        return " ".join([f"{attr.key}:{attr.value}" for attr in self.attrs])

    def __str__(self) -> str:
        return self.elem


class Tree:
    """Create a Tree from Element objects.
    A Tree object is a ">" separated list of Elements.
    The ">" denotes a parent-child relationship with the left Element being the parent of the Element on the right.
    """

    def __init__(self, *elems: Element):
        self.elems = list(elems)
        self.tree: str = self.from_elems()

    def from_elems(self) -> str:
        return " > ".join(str(elem) for elem in self.elems)

    def __str__(self) -> str:
        return self.tree
