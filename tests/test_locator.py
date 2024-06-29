import pytest

from locator import (
    Attribute,
    BUTTON,
    CLASS,
    TEXT,
    COMBO,
    LIST_ITEM,
    ID,
    NAME,
    make_elem,
    make_tree,
)


@pytest.mark.parametrize(
    "attrs, expected",
    [
        ((ID("ID 0"),), 'id:"ID 0"'),
        ((CLASS(" "),), 'class:" "'),
        (
            (ID("negateButton"), BUTTON),
            "id:negateButton type:button",
        ),
        ((Attribute._id(""), TEXT), "id: type:text"),
        (
            (Attribute._name(" NAME X "), TEXT),
            'name:" NAME X " type:text',
        ),
        (
            (Attribute._class("C_105 "), COMBO),
            'class:"C_105 " type:combobox',
        ),
    ],
)
def test_multiple_attributes_locator(attrs, expected: str) -> None:
    assert make_elem(*attrs) == expected


@pytest.mark.parametrize(
    "attr, expected",
    [
        (ID("ID 0"), 'id:"ID 0"'),
        (CLASS(" "), 'class:" "'),
        (NAME(" _my name-"), 'name:" _my name-"'),
        (COMBO, "type:combobox"),
        (TEXT, "type:text"),
        (BUTTON, "type:button"),
        (LIST_ITEM, "type:listItem"),
    ],
)
def test_single_attribute_locator(attr, expected: str) -> None:
    assert make_elem(attr) == expected


@pytest.mark.parametrize(
    "attr, expected",
    [
        (Attribute._id("ID 0"), 'id:"ID 0"'),
        (Attribute._class(" "), 'class:" "'),
        (Attribute._name(" _my name-"), 'name:" _my name-"'),
        (COMBO, "type:combobox"),
        (TEXT, "type:text"),
        (BUTTON, "type:button"),
        (LIST_ITEM, "type:listItem"),
    ],
)
def test_single_attribute_as_string(attr, expected: str) -> None:
    assert make_elem(attr) == expected
    assert f"{attr}" == expected


def test_create_locator_from_list() -> None:
    loc = [
        Attribute._id("I D"),
        BUTTON,
        Attribute._class("C-7"),
        Attribute._name("long-name-47"),
        Attribute._type("ty pe"),
    ]
    assert (
        make_elem(*loc)
        == 'id:"I D" type:button class:C-7 name:long-name-47 type:"ty pe"'
    )


def test_create_locator_from_tuple() -> None:
    elem = (
        BUTTON,
        Attribute._id("ID-3"),
        Attribute._class("buttonClass"),
        Attribute._name("long name 47"),
    )
    assert (
        make_elem(*elem) == 'type:button id:ID-3 class:buttonClass name:"long name 47"'
    )


@pytest.mark.parametrize(
    "elems, expected",
    [
        (
            (BUTTON, Attribute._id("ID"), Attribute._name("NAME ")),
            'type:button > id:ID > name:"NAME "',
        ),
        (
            (Attribute._id("ID-55"),),
            "id:ID-55",
        ),
    ],
)
def test_create_locator_tree(elems, expected: str) -> None:
    assert make_tree(*elems) == expected
