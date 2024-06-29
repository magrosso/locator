import pytest

from locator import (
    Attribute,
    BUTTON,
    CLASS,
    TEXT,
    COMBO,
    LIST_ITEM,
    ID,
    TYPE,
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
        ((ID(""), TEXT), 'id:"" type:text'),
        (
            (NAME(" NAME X "), TEXT),
            'name:" NAME X " type:text',
        ),
        (
            (CLASS("C_105 "), COMBO),
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
        (ID("ID 0"), 'id:"ID 0"'),
        (CLASS(" "), 'class:" "'),
        (NAME(" _my name-"), 'name:" _my name-"'),
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
        ID("I D"),
        BUTTON,
        CLASS("C-7"),
        NAME("long-name-47"),
        TYPE("ty pe"),
    ]
    assert (
        make_elem(*loc)
        == 'id:"I D" type:button class:C-7 name:long-name-47 type:"ty pe"'
    )


def test_create_locator_from_tuple() -> None:
    elem = (
        BUTTON,
        ID("ID-3"),
        CLASS("buttonClass"),
        NAME("long name 47"),
    )
    assert (
        make_elem(*elem) == 'type:button id:ID-3 class:buttonClass name:"long name 47"'
    )


@pytest.mark.parametrize(
    "elems, expected",
    [
        (
            (BUTTON, ID("ID"), NAME("NAME ")),
            'type:button > id:ID > name:"NAME "',
        ),
        (
            (ID("ID-55"),),
            "id:ID-55",
        ),
    ],
)
def test_create_locator_tree(elems, expected: str) -> None:
    assert make_tree(*elems) == expected
