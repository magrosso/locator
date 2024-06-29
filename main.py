from enum import Enum, unique
from locator import (
    Attribute,
    CLASS,
    TYPE,
    ID,
    NAME,
    BUTTON,
    make_elem,
    make_tree,
    elem_dict,
)


loc_4 = Attribute._name("N")

a1 = TYPE("a1")
a2 = CLASS("a2")

e1: str = make_elem(BUTTON)
e2: str = make_elem(CLASS("C"), ID("id"), NAME("N"))
e3: str = make_elem(a1, a2)

t1: str = make_tree(e3, e2, e1)
t2: str = make_tree(e1)
t3: str = make_tree(ID("ID-33"), NAME(" N7"), BUTTON)


@unique
class Locs(Enum):
    L1 = make_tree(ID("ID-33"), NAME(" N7"), BUTTON)
    L2 = make_elem(ID("ID-33"), NAME(" N7"), BUTTON)
    L3 = make_elem(ID("ID 0"))
    L4 = make_tree(ID("ID 1"))


for num, loc in enumerate(Locs, 1):
    print(f"{num}: '{loc.value}'")

print(elem_dict(BUTTON, CLASS("2")))
