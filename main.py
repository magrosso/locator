from locator import Tree, Attribute, Element, BUTTON, COMBO, TEXT

elem_1 = Element(BUTTON)
elem_2 = Element(COMBO, Attribute.from_id("ID-2"))
tree_1 = Tree(elem_1, elem_2)
tree_2 = Tree(
    Element(Attribute.from_name("name"), TEXT),
    Element(BUTTON, Attribute.from_class("CLx3")),
)
tree_3 = Tree(Attribute.from_id("locator with id only"))


def print_element(elem: str | Element) -> None:
    if isinstance(elem, Element):
        elem = str(elem)
    print(f"Element: {elem}")


def print_tree(tree: str | Tree) -> None:
    if isinstance(tree, Tree):
        tree = str(tree)
    print(f"Tree: {tree}")


for elem in elem_1, elem_2:
    print_element(elem)

for tree in (tree_1, tree_2, tree_3):
    print_tree(tree)
