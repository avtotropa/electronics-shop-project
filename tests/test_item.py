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


def test_instantiate_from_csv():
    # Подготовим csv-файл с данными для тестирования
    with open('test_items.csv', 'w', encoding='cp1251') as f:
        f.write("name,price,quantity\n")
        f.write("товар1,10,2\n")
        f.write("товар2,5,3\n")
        f.write("товар3,2,10\n")

    # Проверяем создание экземпляров класса Item из csv-файла
    Item.instantiate_from_csv('test_items.csv')
    assert len(Item.all) == 3
    assert Item.all[0].name == "товар1"
    assert Item.all[1].price == 5
    assert Item.all[2].quantity == 10

    # Удаляем временный csv-файл
    import os
    os.remove('test_items.csv')


def test_string_to_number():
    # Проверяем преобразование числа-строки в число
    assert Item.string_to_number("10") == 10
    assert Item.string_to_number("3.14") == 3
    assert Item.string_to_number("-5") == -5
    assert Item.string_to_number("0") == 0
    assert Item.string_to_number("1000") == 1000

    # Проверяем обработку ошибки при некорректном значении
    with pytest.raises(ValueError):
        Item.string_to_number("не число")
