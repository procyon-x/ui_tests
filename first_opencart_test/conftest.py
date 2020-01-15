# -*- coding: utf-8 -*-
"""Модуль с фикстурами для теста, проверяющего, что пользователь находится на странице Opencart"""
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions


def pytest_addoption(parser):
    """Функция, содержащая в себе параметры для передачи в командную строку"""
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
def driver(request):
    """Функция, запускающая разные браузеры, в зависимости от того, какой будет выбран через командную строку"""
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX
        options = FirefoxOptions()
        options.add_argument("--headless")
        wd = webdriver.Firefox(capabilities=capabilities, options=options)
    elif browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--headless")
        wd = webdriver.Chrome(options=options)
    else:
        capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        wd = webdriver.Ie(capabilities=capabilities)
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def url_opencart(request):
    """Функция для передачи url через командную строку"""
    base_url = request.config.getoption("--url")
    return base_url
