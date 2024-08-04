from enum import Enum, StrEnum, auto


class LocKey(StrEnum):
    ID = auto()
    TYPE = auto()
    CLASS = auto()
    NAME = auto()


def _make_attr(key: LocKey, value: str) -> str:
    value: str = f'"{value}"' if " " in value or not value else value
    return f"{key.value}:{value}"


def and_cat(*attrs: str) -> str:
    return " ".join(attrs)


def tree_cat(*attrs: str) -> str:
    return " > ".join(attrs)


def id_(id_val: str) -> str:
    return _make_attr(key=LocKey.ID, value=id_val)


def name_(name_val: str) -> str:
    return _make_attr(key=LocKey.NAME, value=name_val)


def type_(type_val: str) -> str:
    return _make_attr(key=LocKey.TYPE, value=type_val)


def class_(class_val: str) -> str:
    return _make_attr(key=LocKey.CLASS, value=class_val)


# Type element shortcuts
BUTTON: str = "button"
TEXT: str = "text"
COMBO: str = "combobox"
LIST_ITEM: str = "listItem"
