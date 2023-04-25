import pytest
from src.item import Item
from src.phone import Phone

@pytest.fixture
def test_class_item():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def test_class_phone():
    return Phone("Samsung", 80000, 10, 2)