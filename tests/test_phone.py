def test_phone(test_class_phone):
    assert test_class_phone.name == "Samsung"
    assert test_class_phone.price == 80000
    assert test_class_phone.quantity == 10
    assert test_class_phone.number_of_sim == 2


def test_str(test_class_phone):
    assert str(test_class_phone) == "Samsung"


def test_repr(test_class_phone):
    assert repr(test_class_phone) == "Phone('Samsung', 80000, 10, 2)"


def test_phone_setter(test_class_phone):
    assert test_class_phone.number_of_sim == 2
    test_class_phone.number_of_sim = 1
    assert test_class_phone.number_of_sim == 1
    test_class_phone.number_of_sim = 0
    assert test_class_phone.number_of_sim == 1