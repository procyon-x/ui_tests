import pytest
import math


@pytest.fixture(scope='session')
def greeting():
    print('Hello! Let us start this session!')
    yield
    print('This session is over, bye-bye!')


@pytest.fixture(scope='module')
def homework():
    print('This module contains tests for homework')
    yield
    print('\nThis module is over')


@pytest.fixture(scope='class')
def class_scope():
    print('These tests located in test class')
    yield
    print('\nClass is closed')


@pytest.fixture(scope='function')
def function_fixture():
    print('Now this test starts!')
    yield
    print('\nTest passed, amazing!')


@pytest.fixture()
def hello():
    def _method(name):
        return f"Hello, {name}"

    return _method


@pytest.fixture()
def pi_value():
    return math.pi


@pytest.fixture()
def length():
    return len('Hello')


@pytest.fixture()
def numbers():
    i = 0
    while i < 5:
        i += 1
    return i


@pytest.fixture()
def some_list():
    my_list = list(range(10))
    return my_list


@pytest.fixture
def calculate_it():
    def _method(a, b):
        return a * b

    return _method


@pytest.fixture()
def names():
    names_list = ["John", "Mary", "Alice"]
    return names_list


@pytest.fixture()
def my_dict():
    dict_1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
    print('\n I am your eight test!')
    return dict_1


class MyClass:

    def square_triangle(self, a, h):
        return (a * h) // 2

    def my_sum(self, a_sum):
        return 5 + a_sum


@pytest.fixture()
def my_class_fixture():
    return MyClass()
