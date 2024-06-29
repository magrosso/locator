from typing import Self, Callable
from enum import Enum


class Attribute:
    """Locator attribute of format <key>:<value>"""

    class AttrKey(Enum):
        ID = "id"
        TYPE = "type"
        CLASS = "class"
        NAME = "name"

    def __init__(self, key: AttrKey, value: str):
        self._key: str = key.value
        self._value: str = f'"{value}"' if " " in value or not value else value

    @property
    def as_dict(self) -> dict[str, str]:
        return {self._key: self._value}

    @property
    def as_string(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self._key}:{self._value}"

    # Create Attribute as objects
    @classmethod
    def _id(cls, id_val: str) -> Self:
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

    # Create Attribute as string
    @classmethod
    def _id_str(cls, id_val: str) -> str:
        return cls._id(id_val=id_val).as_string

    @classmethod
    def _name_str(cls, name_val: str) -> str:
        return cls._name(name_val=name_val).as_string

    @classmethod
    def _type_str(cls, type_val: str) -> str:
        return cls._type(type_val=type_val).as_string

    @classmethod
    def _class_str(cls, class_val: str) -> str:
        return cls._class(class_val=class_val).as_string


# Constant Attribute shortcuts returning string
BUTTON: str = Attribute._type(type_val="button").as_string  # "type:button"
TEXT: str = Attribute._type(type_val="text").as_string  # "type:text"
COMBO: str = Attribute._type(type_val="combobox").as_string  # "type:combobox"
LIST_ITEM: str = Attribute._type(type_val="listItem").as_string  # "type:listItem"

# Attribute shortcuts: functions returning str
ID: Callable[[str], str] = Attribute._id_str  # "id:<id_value>"
TYPE: Callable[[str], str] = Attribute._type_str  # "type:<typevalue>"
CLASS: Callable[[str], str] = Attribute._class_str  # "class:<class_value>"
NAME: Callable[[str], str] = Attribute._name_str  # "name:<name_value>"


def _cat_attributes(*elems, cat_op: str) -> str:
    return cat_op.join(elems)


def elem_dict(*elems) -> list[dict[str, str]]:
    """Create a list of dictionaries

    Returns:
        dict[str, str]: _description_
    """
    return [elem.as_dict() for elem in elems]


def make_elem(*elems) -> str:
    return _cat_attributes(*elems, cat_op=" ")


def make_tree(*elems) -> str:
    return _cat_attributes(*elems, cat_op=" > ")
