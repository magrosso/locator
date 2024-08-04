from enum import Enum, StrEnum, auto
from typing import Callable


class Loc:
    """Locator attribute of format <key>:<value>"""

    class CatOp(Enum):
        AND = " "
        PARENT = " > "

    class LocKey(StrEnum):
        ID = auto()
        TYPE = auto()
        CLASS = auto()
        NAME = auto()

    def __init__(self, key: LocKey, value: str):
        self._key: str = key.value
        self._value: str = f'"{value}"' if " " in value or not value else value

    @classmethod
    def add(cls, *attrs: str) -> str:
        return cls._cat(*attrs, cat_op=Loc.CatOp.AND)

    @classmethod
    def tree(cls, *attrs: str) -> str:
        return cls._cat(*attrs, cat_op=Loc.CatOp.PARENT)

    @classmethod
    def _cat(cls, *attrs: str, cat_op: CatOp) -> str:
        return cat_op.value.join(attrs)

    @property
    def as_dict(self) -> dict[str, str]:
        return {self._key: self._value}

    @property
    def as_string(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self._key}:{self._value}"

    @classmethod
    def _id_str(cls, id_val: str) -> str:
        return cls(Loc.LocKey.ID, id_val).as_string

    @classmethod
    def _name_str(cls, name_val: str) -> str:
        return cls(Loc.LocKey.NAME, name_val).as_string

    @classmethod
    def _type_str(cls, type_val: str) -> str:
        return cls(Loc.LocKey.TYPE, type_val).as_string

    @classmethod
    def _class_str(cls, class_val: str) -> str:
        return cls(Loc.LocKey.CLASS, class_val).as_string

# shortcuts
ID: Callable[[str], str] = Loc._id_str  # "id:<id_value>"
TYPE: Callable[[str], str] = Loc._type_str  # "type:<value>"
CLASS: Callable[[str], str] = Loc._class_str  # "class:<class_value>"
NAME: Callable[[str], str] = Loc._name_str  # "name:<name_value>"

# Type element shortcuts
BUTTON: str = TYPE("button")  # "type:button"
TEXT: str = TYPE("text")  # "type:text"
COMBO: str = TYPE("combobox")  # "type:combobox"
LIST_ITEM: str = TYPE("listItem")  # "type:listItem"






