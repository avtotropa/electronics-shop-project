"""Здесь надо написать тесты с использованием pytest для модуля item."""

import unittest
from src.item import Item

class ItemTests(unittest.TestCase):
    def setUp(self):
        self.item = Item("Смартфон", 10.0, 5)

    def test_calculate_total_price(self):
        total_price = self.item.calculate_total_price()
        self.assertEqual(total_price, 50.0)

    def test_apply_discount(self):
        self.item.apply_discount(0.15)
        self.assertEqual(self.item.price, 8.5)

if __name__ == '__main__':
    unittest.main()

