from enum import Enum, StrEnum, auto
from typing import NamedTuple


class LocKey(StrEnum):
    ID = auto()
    TYPE = auto()
    CLASS = auto()
    NAME = auto()


# Type element shortcuts
class Type(Enum):
    BUTTON: str = "button"
    TEXT: str = "text"
    COMBO: str = "combobox"
    LIST_ITEM: str = "listItem"


class Attribute(NamedTuple):
    key: LocKey
    value: str

    def __str__(self):
        value: str = f'"{self.value}"' if " " in self.value or not self.value else self.value
        return f"{self.key.value}:{value}"


def and_cat(*attrs: str) -> str:
    return " ".join(attrs)


def tree_cat(*attrs: str) -> str:
    return " > ".join(attrs)


def id(id_val: str) -> str:
    return str(Attribute(key=LocKey.ID, value=id_val))


def name(name_val: str) -> str:
    return str(Attribute(key=LocKey.NAME, value=name_val))


def type(type_val: Type) -> str:
    return str(Attribute(key=LocKey.TYPE, value=type_val.value))


def cls(class_val: str) -> str:
    return str(Attribute(key=LocKey.CLASS, value=class_val))
