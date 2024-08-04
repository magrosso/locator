from enum import Enum, unique

from locator import and_cat, tree_cat, name_, class_, type_, id_, BUTTON, TEXT, COMBO, LIST_ITEM

a1: str = f"{type_("a1")} {name_("")}"
a2: str = class_("a2")

e1: str = and_cat(type_(BUTTON))
e2: str = and_cat(class_("C"), id_("id_"), name_("N"))
e3: str = and_cat(a1, a2)

t1: str = tree_cat(e3, e2, e1)
t2: str = tree_cat(e1)
t3: str = tree_cat(id_("id_-33"), name_(" N7"), type_(BUTTON))


# @unique
class Locator(Enum):
    LOC_1 = tree_cat(id_("id_-33"), name_(" N7"), type_(BUTTON))
    LOC_2 = and_cat(id_("id_-33"), name_(" N7"), type_(BUTTON))
    LOC_3 = id_("id_ 0")
    LOC_4 = tree_cat(id_("id_ 1"))
    LOC_5 = tree_cat(id_("id_ 1"), and_cat(id_("id_ iix"), name_("n0")))
    LOC_6 = and_cat(id_("id_ 1"), tree_cat(id_("is iiu"), name_("n-669")))
    LOC_8 = LOC_3
    LOC_7 = and_cat(LOC_1, LOC_2, LOC_3)


print(Locator.LOC_1.value)
print(Locator.LOC_2.value)
print(Locator.LOC_3.value)
print(Locator.LOC_4.value)
print(Locator.LOC_5.value)
print(Locator.LOC_6.value)
print(Locator.LOC_7.value)
print(Locator.LOC_8.value)

# for num, loc in enumerate(Locator, 1):
#     print(f"{num}: '{loc.value}'")
