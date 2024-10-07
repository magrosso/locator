from enum import Enum

# from locator import and_cat, tree_cat, name, class_, type_, id, Type, Attribute, LocKey

import locator

a1: str = f"{locator.type(locator.Type.TEXT)} {locator.name("")}"
a2: str = locator.cls("a2")

e1: str = locator.and_cat(locator.type(locator.Type.BUTTON))
e2: str = locator.and_cat(locator.cls("C"), locator.id("id"), locator.name("N"))
e3: str = locator.and_cat(a1, a2)

t1: str = locator.tree_cat(e3, e2, e1)
t2: str = locator.tree_cat(e1)
t3: str = locator.tree_cat(locator.id("id-33"), locator.name(" N7"), locator.type(locator.Type.BUTTON))


# @unique
class Locator(Enum):
    LOC_1: str = locator.tree_cat(locator.id("id-33"), locator.name(" N7"), locator.type(locator.Type.BUTTON))
    LOC_2: str = locator.and_cat(locator.id("id-33"), locator.name(" N7"), locator.type(locator.Type.BUTTON))
    LOC_3: str = locator.id("id 0")
    LOC_4: str = locator.tree_cat(locator.cls("C "), locator.id("id 1"))
    LOC_5: str = locator.tree_cat(locator.id("id 1"), locator.and_cat(locator.id("id iix"), locator.name("n0")))
    LOC_6: str = locator.and_cat(locator.id("id 1"), locator.tree_cat(locator.id("is iiu"), locator.name("n-669")))
    LOC_8: str = LOC_3
    LOC_7: str = locator.and_cat(LOC_1, LOC_2, LOC_3)
    LOC_100: str = locator.Attribute(key=locator.LocKey.ID, value="idval")


print(Locator.LOC_1.value)
print(Locator.LOC_2.value)
print(Locator.LOC_3.value)
print(Locator.LOC_4.value)
print(Locator.LOC_5.value)
print(Locator.LOC_6.value)
print(Locator.LOC_7.value)
print(Locator.LOC_8.value)
print(Locator.LOC_100.value)


# for num, loc in enumerate(Locator, 1):
#     print(f"{num}: '{loc.value}'")
