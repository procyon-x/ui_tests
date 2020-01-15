# -*- coding: utf-8 -*-
"""Модуль с фикстурами для запуска тестов Opencart"""
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Создание параметров для передачи в командную строку"""
    parser.addoption(
        "--browser",
        action="store",
        default="Internet Explorer",
        help="Browser name")

    parser.addoption(
        "--url",
        action="store",
        default="http://localhost",
        help="This is request url")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    """Фикстура для запуска браузера и возможности выбора его через передачу параметра в консоли"""
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        wd = webdriver.Chrome()
    elif browser == "firefox":
        wd = webdriver.Firefox()
    else:
        wd = webdriver.Ie()

    request.addfinalizer(wd.quit)
    wd.get(request.config.getoption("--url"))

    return wd
