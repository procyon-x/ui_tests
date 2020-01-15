# -*- coding: utf-8 -*-
"""Модуль с парсером и фикстурами для запуска тестов Opencart/admin"""
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Создание параметра для выбора браузера и времени ожидания через командную строку"""
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Browser name")

    parser.addoption(
        "--url",
        action="store",
        default="http://localhost/Opencart/",
        help="This is request url")

    parser.addoption(
        "--wait",
        action="store",
        default=0,
        help="Waiting time")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    """Фикстура для запуска и выбора браузера через консоль. Добавлена возможность выставить время ожидания."""
    browser = request.config.getoption("--browser")
    waiting_time = request.config.getoption("--wait")
    if browser == "Ie":
        wd = webdriver.Ie()
    elif browser == "chrome":
        wd = webdriver.Chrome()
        wd.maximize_window()
    else:
        wd = webdriver.Firefox()
        wd.maximize_window()

    request.addfinalizer(wd.quit)
    wd.implicitly_wait(waiting_time)
    wd.get(request.config.getoption("--url"))
    return wd


@pytest.fixture()
def test_login(browser):
    """Функция логина в админскую  панель"""
    browser.get(browser.current_url + 'admin')
    username = browser.find_element_by_id('input-username')
    username.clear()
    username.send_keys('admin')
    password = browser.find_element_by_id('input-password')
    password.clear()
    password.send_keys('admin')
    browser.find_element_by_class_name('btn-primary').click()
