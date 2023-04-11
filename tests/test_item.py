"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

def test_calculate_total_price():
    # Тест 1: Количество 1, Цена 10.0
    item = Item("Тестовый Товар", 10.0, 1)
    assert item.calculate_total_price() == 10.0

    # Тест 2: Количество 0, Цена 5.0
    item = Item("Тестовый Товар", 5.0, 0)
    assert item.calculate_total_price() == 0.0

    # Тест 3: Количество 5, Цена 2.5
    item = Item("Тестовый Товар", 2.5, 5)
    assert item.calculate_total_price() == 12.5

def test_apply_discount():
    # Тест 1: Коэффициент скидки 0.9
    item = Item("Тестовый Товар", 10.0, 1)
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0

    # Тест 2: Коэффициент скидки 0.5
    item = Item("Тестовый Товар", 20.0, 3)
    item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 10.0

def test_item_creation():
    # Тест 1: Проверка имени, цены и количества товара
    item = Item("Тестовый Товар", 10.0, 3)
    assert item.name == "Тестовый Товар"
    assert item.price == 10.0
    assert item.quantity == 3

    # Тест 2: Проверка добавления товара в список 'all'
    assert item in Item.all
    assert len(Item.all) == 1
