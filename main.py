from locator import Attribute, CLASS, ID, NAME, BUTTON, make_elem, make_tree


loc_4 = Attribute._name("N")

a1 = Attribute._type("a1")
a2 = Attribute._class("a2")

e1: str = make_elem(BUTTON)
e2: str = make_elem(CLASS("C"), ID("id"), NAME("N"))
e3: str = make_elem(a1, a2)

t1: str = make_tree(e3, e2, e1)
t2: str = make_tree(e1)
t3: str = make_tree(ID("ID-33"), NAME(" N7"), BUTTON)


def print_locator(elem: str) -> None:
    print(f"\tLocator: '{elem}'")


for loc in e1, e2, e3, t1, t2, t3:
    print_locator(loc)
