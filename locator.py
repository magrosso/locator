from enum import Enum
from typing import Self


class Loc:
    class Key(Enum):
        ID = "id"
        CLASS = "class"
        TYPE = "type"
        NAME = "name"

    class Op(Enum):
        AND = "and"
        PARENT = ">"

    def __init__(self, key: Key = Key.ID, val: str = "") -> None:
        self.key = key
        self.val = val
        if " " in val:
            # empty values or values with space characters must be quoted!
            self.loc = f'{self.key}:"{self.val}"'
        else:
            self.loc = f"{self.key}:{self.val}"

    def __add__(self, rhs: Self) -> Self:
        self.loc = f"{self.loc} {Loc.Op.AND.value} {rhs}"
        return self

    def __gt__(self, rhs: Self) -> Self:
        self.loc = f"{self.loc} {Loc.Op.PARENT.value} {rhs}"
        return self

    def __str__(self) -> str:
        return self.loc

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.key}, {self.val})"


class LocType(Enum):
    BUTTON = Loc(Loc.Key.TYPE, "BUTTON")
    EDIT = Loc(Loc.Key.TYPE, "EDIT")
    COMBO_BOX = Loc(Loc.Key.TYPE, "COMBOBOX")


class Locator(Enum):
    LOC_1 = Loc(Loc.Key.ID, " 1 ") + Loc(Loc.Key.NAME, "")
    LOC_2 = Loc(Loc.Key.ID, "ID 4")

    LOC_3 = (
        Loc(Loc.Key.ID, "ID 1")
        + Loc(Loc.Key.CLASS, "CLASS 2")
        + Loc(Loc.Key.NAME, "NAME 3")
    )

    LOC_4 = LocType.BUTTON.value + Loc(Loc.Key.CLASS, "CLASS 332") + Loc(
        Loc.Key.NAME, "NAME-4"
    ) > Loc(Loc.Key.ID, "_id_")

    LOC_5 = LocType.COMBO_BOX.value
    LOC_6 = LocType.BUTTON.value + Loc(Loc.Key.ID, "U")
    LOC_7 = LocType.EDIT.value > Loc(Loc.Key.NAME)


def main() -> None:
    loc_x = Loc(Loc.Key.ID, "I3")
    loc_y = loc_x + Loc(Loc.Key.CLASS, "C")
    loc_z = Loc(Loc.Key.CLASS, "C") + loc_x
    print(loc_x)
    print(loc_y)
    print(loc_z)
    print(Locator.LOC_1.value)
    print(Locator.LOC_2.value)
    print(Locator.LOC_3.value)
    print(Locator.LOC_4.value)
    print(Locator.LOC_5.value)
    print(Locator.LOC_6.value)
    print(Locator.LOC_7.value)


if __name__ == "__main__":
    main()
