import pytest

from src.locator.locator import (
    BUTTON,
    class_,
    COMBO,
    id_,
    LIST_ITEM,
    name_,
    TEXT,
    type_,
    cat_and,
    and_cat,
    tree_cat,
)


@pytest.mark.parametrize(
    "attrs, expected",
    [
        ((id_("ID 0"),), 'id:"ID 0"'),
        ((class_(" "),), 'class:" "'),
        (
            (id_("negateButton"), BUTTON),
            "id:negateButton type:button",
        ),
        ((id_(""), TEXT), 'id:"" type:text'),
        (
            (name_(" NAME X "), TEXT),
            'name:" NAME X " type:text',
        ),
        (
            (class_("C_105 "), COMBO),
            'class:"C_105 " type:combobox',
        ),
    ],
)
def test_multiple_attributes_locator(attrs, expected: str) -> None:
    assert and_cat(*attrs) == expected


@pytest.mark.parametrize(
    "attr, expected",
    [
        (id_("ID 0"), 'id:"ID 0"'),
        (class_(" "), 'class:" "'),
        (name_(" _my name-"), 'name:" _my name-"'),
        (COMBO, "type:combobox"),
        (TEXT, "type:text"),
        (BUTTON, "type:button"),
        (LIST_ITEM, "type:listItem"),
    ],
)
def test_single_attribute_locator(attr, expected: str) -> None:
    assert and_cat(attr) == expected


@pytest.mark.parametrize(
    "attr, expected",
    [
        (id_("ID 0"), 'id:"ID 0"'),
        (class_(" "), 'class:" "'),
        (name_(" _my name-"), 'name:" _my name-"'),
        (COMBO, "type:combobox"),
        (TEXT, "type:text"),
        (BUTTON, "type:button"),
        (LIST_ITEM, "type:listItem"),
    ],
)
def test_single_attribute_as_string(attr, expected: str) -> None:
    assert and_cat(attr) == expected
    assert f"{attr}" == expected


def test_create_locator_from_list() -> None:
    loc = [
        id_("I D"),
        BUTTON,
        class_("C-7"),
        name_("long-name-47"),
        type_("ty pe"),
    ]
    assert (
            and_cat(*loc)
            == 'id:"I D" type:button class:C-7 name:long-name-47 type:"ty pe"'
    )


def test_create_locator_from_tuple() -> None:
    elem = (
        BUTTON,
        id_("ID-3"),
        class_("buttonClass"),
        name_("long name 47"),
    )
    assert (
            and_cat(*elem) == 'type:button id:ID-3 class:buttonClass name:"long name 47"'
    )


@pytest.mark.parametrize(
    "elems, expected",
    [
        (
            (BUTTON, id_("ID"), name_("NAME ")),
            'type:button > id:ID > name:"NAME "',
        ),
        (
            (id_("ID-55"),),
            "id:ID-55",
        ),
    ],
)
def test_create_locator_tree(elems, expected: str) -> None:
    assert tree_cat(*elems) == expected


@pytest.mark.parametrize(
    "left_attr, right_attr, expected",
    [
        (
                BUTTON,
                id_("ID"),
            "type:button id:ID",
        ),
    ],
)
def test_addition(left_attr, right_attr, expected) -> None:
    assert cat_and(left_attr, right_attr) == expected
