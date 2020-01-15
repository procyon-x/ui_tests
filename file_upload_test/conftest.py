# -*- coding: utf-8 -*-
"""Модуль с парсером и фикстурой для запуска теста Opencart"""

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Создание параметра для выбора браузера через командную строку"""
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    """Фикстура для запуска браузера и возможности выбрать нужный через передачу параметра в консоли"""
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        wd = webdriver.Chrome()
    else:
        wd = webdriver.Firefox()

    request.addfinalizer(wd.quit)
    wd.maximize_window()
    return wd


@pytest.fixture()
def test_login(browser):
    """Функция логина в админскую  панель"""
    browser.get('http://localhost/Opencart/admin/')
    username = browser.find_element_by_id('input-username')
    username.clear()
    username.send_keys('admin')
    password = browser.find_element_by_id('input-password')
    password.clear()
    password.send_keys('admin')
    browser.find_element_by_class_name('btn-primary').click()
