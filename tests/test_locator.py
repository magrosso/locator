import pytest
from locator import Element, Attribute, Tree, BUTTON, TEXT, COMBO


@pytest.mark.parametrize(
    "attrs, expected",
    [
        ((Attribute.from_id("ID 0"),), 'id:"ID 0"'),
        ((Attribute.from_class(" "),), 'class:" "'),
        (
            (Attribute.from_id("negateButton"), BUTTON),
            "id:negateButton type:button",
        ),
        ((Attribute.from_id(""), TEXT), "id: type:text"),
        (
            (Attribute.from_name(" NAME X "), TEXT),
            'name:" NAME X " type:text',
        ),
        (
            (Attribute.from_class("C_105 "), COMBO),
            'class:"C_105 " type:combobox',
        ),
    ],
)
def test_multiple_attributes_locator(attrs, expected: str) -> None:
    assert str(Element(*attrs)) == expected


@pytest.mark.parametrize(
    "attr, expected",
    [
        (Attribute.from_id("ID 0"), 'id:"ID 0"'),
        (Attribute.from_class(" "), 'class:" "'),
        (Attribute.from_name(" _my name-"), 'name:" _my name-"'),
        (Attribute.combo(), "type:combobox"),
        (TEXT, "type:text"),
        (Attribute.button(), "type:button"),
        (Attribute.list_item(), "type:listItem"),
    ],
)
def test_single_attribute_locator(attr, expected: str) -> None:
    assert str(Element(attr)) == expected


@pytest.mark.parametrize(
    "attr, expected",
    [
        (Attribute.from_id("ID 0"), 'id:"ID 0"'),
        (Attribute.from_class(" "), 'class:" "'),
        (Attribute.from_name(" _my name-"), 'name:" _my name-"'),
        (Attribute.combo(), "type:combobox"),
        (TEXT, "type:text"),
        (Attribute.button(), "type:button"),
        (Attribute.list_item(), "type:listItem"),
    ],
)
def test_single_attribute_as_string(attr, expected: str) -> None:
    assert str(attr) == expected
    assert f"{attr}" == expected


def test_create_locator_from_list() -> None:
    loc = [
        Attribute.from_id("I D"),
        BUTTON,
        Attribute.from_class("C-7"),
        Attribute.from_name("long-name-47"),
        Attribute.from_type("ty pe"),
    ]
    assert (
        str(Element(*loc))
        == 'id:"I D" type:button class:C-7 name:long-name-47 type:"ty pe"'
    )


def test_create_locator_from_tuple() -> None:
    elem = (
        BUTTON,
        Attribute.from_id("ID-3"),
        Attribute.from_class("buttonClass"),
        Attribute.from_name("long name 47"),
    )
    assert (
        str(Element(*elem))
        == 'type:button id:ID-3 class:buttonClass name:"long name 47"'
    )


def test_create_locator_tree() -> None:
    e1 = Element(BUTTON)
    e2 = Element(TEXT)
    e3 = Element(COMBO)
    e4 = Element(Attribute.from_id("att"))
    assert (
        str(Tree(e1, e2, e3, e4)) == "type:button > type:text > type:combobox > id:att"
    )
