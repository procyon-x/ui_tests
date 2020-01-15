# -*- coding: utf-8 -*-
"""Модуль с тестом для Opencart"""


def test_selenium_1(driver, url_opencart):
    """Тест, проверяющий нахождение на главной странице Opencart"""
    driver.get(url_opencart)
    assert driver.title == "Your Store"
    print(driver.title)
    print(driver)
