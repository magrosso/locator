from enum import Enum, StrEnum, auto
from functools import partialmethod
from typing import NamedTuple


class LocKey(StrEnum):
    ID = auto()
    TYPE = auto()
    CLASS = auto()
    NAME = auto()


# Type element shortcuts
class Type(Enum):
    BUTTON: str = "Button"
    CHECK_BOX: str = "CheckBox"
    COMBO_BOX: str = "ComboBox"
    DATA_GRID: str = "DataGrid"
    DATA_ITEM: str = "DataItem"
    EDIT: str = "Edit"
    GROUP: str = "Group"
    LIST: str = "List"
    LIST_ITEM: str = "ListItem"
    MENU_ITEM: str = "MenuItem"
    PANE: str = "Pane"
    PROGRESS_BAR: str = "ProgressBarControl"
    RADIO_BUTTON: str = "RadioButton"
    SLIDER: str = "Slider"
    TAB: str = "Tab"
    TAB_ITEM: str = "TabItem"
    TEXT: str = "Text"
    THUMB: str = "Thumb"
    TOOL_BAR: str = "ToolBarControl"
    WINDOW: str = "Window"


class Attribute(NamedTuple):
    key: LocKey
    value: str

    def __str__(self):
        value: str = f'"{self.value}"' if " " in self.value or not self.value else self.value
        return f"{self.key.value}:{value}"


class Loc:
    @staticmethod
    def and_join(*attrs: str) -> str:
        return " ".join(attrs)

    @staticmethod
    def tree_join(*attrs: str) -> str:
        return " > ".join(attrs)

    @staticmethod
    def id(id_val: str) -> str:
        return str(Attribute(key=LocKey.ID, value=id_val))

    @staticmethod
    def name(name_val: str) -> str:
        return str(Attribute(key=LocKey.NAME, value=name_val))

    @staticmethod
    def cls(class_val: str) -> str:
        return str(Attribute(key=LocKey.CLASS, value=class_val))

    @staticmethod
    def type(type_val: Type) -> str:
        return str(Attribute(key=LocKey.TYPE, value=type_val.value))

    button = partialmethod(type, type_val=Type.BUTTON)
    check_box = partialmethod(type, type_val=Type.CHECK_BOX)
    combo_box = partialmethod(type, type_val=Type.COMBO_BOX)
    data_grid: str = partialmethod(type, type_val=Type.DATA_GRID)
    data_item: str = partialmethod(type, type_val=Type.DATA_ITEM)
    edit = partialmethod(type, type_val=Type.EDIT)
    group = partialmethod(type, type_val=Type.GROUP)
    list = partialmethod(type, type_val=Type.LIST)
    list_item = partialmethod(type, type_val=Type.LIST_ITEM)
    menu_item = partialmethod(type, type_val=Type.MENU_ITEM)
    pane = partialmethod(type, type_val=Type.PANE)
    progress_bar = partialmethod(type, type_val=Type.PROGRESS_BAR)
    radio_button = partialmethod(type, type_val=Type.RADIO_BUTTON)
    slider = partialmethod(type, type_val=Type.SLIDER)
    tab = partialmethod(type, type_val=Type.TAB)
    tab_item = partialmethod(type, type_val=Type.TAB_ITEM)
    text = partialmethod(type, type_val=Type.TEXT)
    thumb = partialmethod(type, type_val=Type.THUMB)
    tool_bar = partialmethod(type, type_val=Type.TOOL_BAR)
    window = partialmethod(type, type_val=Type.WINDOW)
