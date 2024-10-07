from enum import Enum

# from src.locator import and_cat, tree_cat, name, cls, type, id, Type, Attribute, LocKey

from locator_path import Loc, Type, LocKey, Attribute

a1: str = f"{Loc.type(Type.TEXT)} {Loc.name("")}"
a2: str = Loc.cls("a2")

e1: str = Loc.and_cat(Loc.type(Type.BUTTON))
e2: str = Loc.and_cat(Loc.cls("C"), Loc.id("id"), Loc.name("N"))
e3: str = Loc.and_cat(a1, a2)

t1: str = Loc.tree_cat(e3, e2, e1)
t2: str = Loc.tree_cat(e1)
t3: str = Loc.tree_cat(Loc.id("id-33"), Loc.name(" N7"), Loc.type(Type.BUTTON))


# @unique
class Locator(Enum):
    LOC_1: str = Loc.tree_cat(Loc.id("id-33"), Loc.name(" N7"), Loc.type(Type.BUTTON))
    LOC_2: str = Loc.and_cat(Loc.id("id-33"), Loc.name(" N7"), Loc.type(Type.BUTTON))
    LOC_3: str = Loc.id("id 0")
    LOC_4: str = Loc.tree_cat(Loc.cls("C "), Loc.id("id 1"))
    LOC_5: str = Loc.tree_cat(Loc.id("id 1"), Loc.and_cat(Loc.id("id iix"), Loc.name("n0")))
    LOC_6: str = Loc.and_cat(Loc.id("id 1"), Loc.tree_cat(Loc.id("is iiu"), Loc.name("n-669")))
    LOC_8: str = LOC_3
    LOC_7: str = Loc.and_cat(LOC_1, LOC_2, LOC_3)
    LOC_100: str = Attribute(key=LocKey.ID, value="idval")


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
