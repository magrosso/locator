from enum import Enum, StrEnum, auto
from typing import Callable


class Attribute:
    """Locator attribute of format <key>:<value>"""

    class AttrKey(StrEnum):
        ID = auto()
        TYPE = auto()
        CLASS = auto()
        NAME = auto()

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

    # Create Attribute as string
    @classmethod
    def _id_str(cls, id_val: str) -> str:
        return cls(Attribute.AttrKey.ID, id_val).as_string

    @classmethod
    def _name_str(cls, name_val: str) -> str:
        return cls(Attribute.AttrKey.NAME, name_val).as_string

    @classmethod
    def _type_str(cls, type_val: str) -> str:
        return cls(Attribute.AttrKey.TYPE, type_val).as_string

    @classmethod
    def _class_str(cls, class_val: str) -> str:
        return cls(Attribute.AttrKey.CLASS, class_val).as_string


ID: Callable[[str], str] = Attribute._id_str  # "id:<id_value>"
TYPE: Callable[[str], str] = Attribute._type_str  # "type:<typevalue>"
CLASS: Callable[[str], str] = Attribute._class_str  # "class:<class_value>"
NAME: Callable[[str], str] = Attribute._name_str  # "name:<name_value>"

# Type element shortcuts
BUTTON: str = TYPE("button")  # "type:button"
TEXT: str = TYPE("text")  # "type:text"
COMBO: str = TYPE("combobox")  # "type:combobox"
LIST_ITEM: str = TYPE("listItem")  # "type:listItem"


class CatOp(Enum):
    AND = " "
    PARENT = " > "


def cat(*elems: str, cat_op: CatOp) -> str:
    return cat_op.value.join(elems)


def make_elem(*elems: str) -> str:
    return cat(*elems, cat_op=CatOp.AND)


def make_tree(*elems: str) -> str:
    return cat(*elems, cat_op=CatOp.PARENT)
