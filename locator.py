from enum import Enum, auto
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

    def __init__(self, key: Key = "", val: str = "", loc_str: str = "") -> None:
        self.key = key
        self.val = val
        self.loc_str = ""

        if loc_str:
            self.loc_str = loc_str
            return
        if key:
            self.loc_str += f"{key.value}:"
        if val and " " not in val:
            self.loc_str += val
        else:
            # empty values or values with space characters must be quoted!
            self.loc_str += f'"{val}"'

    def __add__(self, rhs: Self) -> Self:
        return Loc(loc_str=f"{self.loc_str} {Loc.Op.AND.value} {rhs.loc_str}")

    def __gt__(self, rhs: Self) -> Self:
        return Loc(loc_str=f"{self.loc_str} {Loc.Op.PARENT.value} {rhs.loc_str}")

    def __str__(self) -> str:
        return self.loc_str

    def __repr__(self) -> str:
        return f"Loc.from_str({self.loc_str})"


class LocType(Enum):
    BUTTON = Loc(Loc.Key.TYPE, "BUTTON")
    EDIT = Loc(Loc.Key.TYPE, "EDIT")
    COMBO_BOX = Loc(Loc.Key.TYPE, "COMBOBOX")


class Locator(Enum):
    LOC_1 = str(Loc(Loc.Key.ID, " 1 ") + Loc(Loc.Key.NAME, ""))
    LOC_2 = str(Loc(Loc.Key.ID, "ID 4"))
    LOC_3 = str(Loc(Loc.Key.ID, "ID 1") + Loc(Loc.Key.CLASS, "CLASS 2") + Loc(Loc.Key.NAME, "NAME 3"))
    LOC_4 = str(
        LocType.BUTTON.value + Loc(Loc.Key.CLASS, "CLASS 332") + Loc(Loc.Key.NAME, "NAME-4") > Loc(Loc.Key.ID, "_id_"))
    LOC_5 = str(LocType.COMBO_BOX.value)
    LOC_6 = str(LocType.BUTTON.value + Loc(Loc.Key.ID, "U"))
    LOC_7 = str(LocType.EDIT.value > Loc(Loc.Key.NAME))


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
