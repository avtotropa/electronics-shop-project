import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Получение названия товара.
        Атрибут является приватным и для доступа к нему используется геттер и сеттер, реализованные
        с помощью @property
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Установка названия товара.
        Проверяет, что длина наименования товара не больше 10 символов.
        """
        if len(name) > 10:
            return f'Длина наименования товара не должна превышать 10 символов.'
            # raise ValueError("Длина наименования товара не должна превышать 10 символов.")
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * Item.pay_rate

    def apply_discount(self, discount: float) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        :param discount: Скидка в процентах (например, 0.15 для 15% скидки).
        """
        self.price = self.price * (1 - discount)

    @classmethod
    def instantiate_from_csv(cls, filename='items.csv') -> None:
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv.
        """
        with open(filename, 'r', encoding='cp1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls.all.append(cls(row['name'], float(row['price']), int(row['quantity'])))


    @staticmethod
    def string_to_number(number: str) -> float:
        """
        Статический метод, возвращающий число из числа-строки.
        :param value: Число в виде строки.
        :return: Число типа float.
        """
        return int(float(number))

    def __str__(self) -> str:
        """
        Возвращает строковое представление товара в магазине.
        :return: Строковое представление товара в магазине.
        """
        return f"{self.name}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление товара в магазине.
        :return: Строковое представление товара в магазине.
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})"
