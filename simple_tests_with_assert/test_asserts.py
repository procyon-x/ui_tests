""" В этом модуле содержится домашнее задание № 2 (введение в PyTest) """


def test_1(hello, greeting, homework):
    """ Этот тест проверяет возможность подстановки имени для приветствия """
    result1 = hello('Newcomer')
    assert result1 == 'Hello, Newcomer'


def test_2(pi_value, function_fixture):
    """ Этот тест проверяет значение Пи """
    assert pi_value == 3.141592653589793


def test_3(length):
    """ Этот тест проверяет длину заданного слова """
    assert length == 5


def test_4(numbers):
    """ Этот тест проверяет результат работы цикла while """
    assert numbers == 5


def test_5(some_list):
    """ Этот тест проверяет максимальное значение в заданном списке """
    assert max(some_list) == 9


def test_6(calculate_it):
    """ Этот тест проверяет результат умножения переданных в параметры чисел """
    result = calculate_it(2, 3)
    assert result == 6


def test_7(names):
    """ Этот тест проверяет, что в заданном списке присутствует указанное имя """
    assert 'Alice' in names


def test_8(my_dict):
    """ Этот тест проверяет соответствие значения определённому ключу в словаре """
    assert my_dict[2] == 'Two'


class TestNewClass:
    """ Просто класс с двумя тестами """

    def test_9(self, my_class_fixture, class_scope):
        """ Этот тест считает площадь треугольника с разными передаваемыми в тест параметрами """

        assert my_class_fixture.square_triangle(100, 100) == 5000

    def test_10(self, my_class_fixture):
        """ Этот тест прибавляет к числу 5 любое переданное в параметры число """
        assert my_class_fixture.my_sum(10) == 15
