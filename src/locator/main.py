from enum import Enum, unique


from locator import (
    BUTTON,
    CLASS,
    ID,
    NAME,
    TYPE,
    Loc,
)

loc_4 = Loc._name_str("N")

a1 = TYPE("a1")
a2 = CLASS("a2")

e1: str = Loc.add(BUTTON)
e2: str = Loc.add(CLASS("C"), ID("id"), NAME("N"))
e3: str = Loc.add(a1, a2)

t1: str = Loc.tree(e3, e2, e1)
t2: str = Loc.tree(e1)
t3: str = Loc.tree(ID("ID-33"), NAME(" N7"), BUTTON)


@unique
class Locator(Enum):
    L1 = Loc.tree(ID("ID-33"), NAME(" N7"), BUTTON)
    L2 = Loc.add(ID("ID-33"), NAME(" N7"), BUTTON)
    L3 = Loc.add(ID("ID 0"))
    L4 = Loc.tree(ID("ID 1"))
    L5 = Loc.tree(ID("ID 1"), Loc.add(ID("id iix"), NAME("n0")))
    L6 = Loc.add(ID("ID 1"), Loc.tree(ID("is iiu"), NAME("n-669")))


for num, loc in enumerate(Locator, 1):
    print(f"{num}: '{loc.value}'")
