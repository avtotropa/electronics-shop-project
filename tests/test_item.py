"""Здесь надо написать тесты с использованием pytest для модуля item."""

"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item(test_class_item):
    """Тестирование создания объекта Item."""
    assert isinstance(test_class_item, Item)
    assert test_class_item.name == "Смартфон"
    assert test_class_item.price == 10000
    assert test_class_item.quantity == 20
    assert test_class_item.calculate_total_price() == 200000
    assert test_class_item.apply_discount() is None
