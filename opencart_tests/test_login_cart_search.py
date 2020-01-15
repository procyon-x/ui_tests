# -*- coding: utf-8 -*-
"""Модуль с тестами для Opencart"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from locators import MainPage
from locators import ProductPage


def test_account_page(browser):
    """Тест, проверяющий, что при переходе по ссылке 'My Account' появляются 'хлебные крошки'."""
    browser.find_element_by_link_text(MainPage.account_link).click()
    browser.find_element_by_class_name("breadcrumb")


def test_input(browser):
    """Тест, проверяющий работу поиска"""
    input_data = browser.find_element_by_class_name(MainPage.search_input_class)
    input_data.send_keys("mac")
    browser.find_element_by_class_name(MainPage.search_button_class).click()
    h2 = browser.find_element_by_tag_name("h2")
    assert h2.text == "Products meeting the search criteria"


def test_add_to_cart(browser):
    """Тест, проверяющий функцию добавления товара в корзину"""
    browser.find_element_by_link_text('iPhone').click()
    input_field = browser.find_element_by_xpath(ProductPage.input_quantity)
    input_field.clear()
    input_field.send_keys("2")
    browser.find_element_by_xpath(ProductPage.add_to_cart).click()
    ActionChains(browser).pause(0.5).perform()
    browser.find_element_by_class_name(ProductPage.alert_success_class)


def test_section_page(browser):
    """Тест для раздела каталога, проверяющий возможность изменить опции отображения и количества товара на странице."""
    browser.find_element_by_link_text('Cameras').click()
    browser.find_element_by_id('list-view').click()
    select = Select(browser.find_element_by_id('input-limit'))
    select.select_by_index(1)


def test_login_page(browser):
    """Тест, проверяющий работу функции логина в админскую панель"""
    username = browser.find_element_by_id('input-username')
    username.clear()
    username.send_keys('admin')
    password = browser.find_element_by_id('input-password')
    password.clear()
    password.send_keys('admin')
    browser.find_element_by_class_name('btn-primary').click()
    h1 = browser.find_element_by_tag_name("h1")
    assert h1.text == "Dashboard"
