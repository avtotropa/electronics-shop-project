"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_calculate_total_price():
    # Ожидаем значение с округленным значением до 2х знаков, после запятой
    # Если у нас какого-то товара не целое число ;)
    item1 = Item("товар1", 10, 2)
    assert round(item1.calculate_total_price(), 2) == 20.0

    item2 = Item("товар2", 5, 3)
    assert round(item2.calculate_total_price(), 2) == 15.0

    item3 = Item("товар3", 2, 10)
    assert round(item3.calculate_total_price(), 2) == 20.0


def test_apply_discount():
    # Ожидаем значение с округленным значением до 2х знаков, после запятой
    item1 = Item("товар1", 10, 2)
    item1.apply_discount(0.1)
    assert round(item1.price, 2) == 9.0

    item2 = Item("товар2", 5, 3)
    item2.apply_discount(0.25)
    assert round(item2.price, 2) == 3.75

    item3 = Item("товар3", 2, 10)
    item3.apply_discount(0.05)
    assert round(item3.price, 2) == 1.9


