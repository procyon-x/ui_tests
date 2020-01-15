# -*- coding: utf-8 -*-
"""Модуль с тестами для страницы Products в админской панели.
Тесты независимы и могут запускаться как отдельно, так и модулем.
В командой строке можно выбрать браузер. По умолчанию - Firefox."""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def test_creation(browser, test_login):
    """Тест для функции создания продукта"""
    browser.find_element_by_link_text("Catalog").click()
    ActionChains(browser).pause(0.5).perform()
    browser.find_element_by_link_text("Products").click()
    browser.find_element_by_xpath("//a[@data-original-title='Add New']").click()
    product_name = browser.find_element_by_id("input-name1")
    product_name.send_keys("Samsung Galaxy A50")
    meta_tag = browser.find_element_by_id("input-meta-title1")
    meta_tag.send_keys("Samsung Galaxy")
    browser.find_element_by_link_text("Data").click()
    model_input = browser.find_element_by_id("input-model")
    model_input.send_keys("Product 123")
    browser.find_element_by_xpath("//button[@data-original-title='Save']").click()
    product_added = browser.find_element_by_class_name("alert-success")
    assert product_added.text == "Success: You have modified products!\n×"
    print(product_added.text)


def test_edition(browser, test_login):
    """Тест для функции редактирования продукта"""
    browser.find_element_by_link_text("Catalog").click()
    ActionChains(browser).pause(0.5).perform()
    browser.find_element_by_link_text("Products").click()
    browser.find_element_by_xpath(
        "//td[text()='Samsung Galaxy A50']/following-sibling::td[@class='text-right']/a").click()
    browser.find_element_by_link_text("Data").click()
    price_input = browser.find_element_by_id("input-price")
    price_input.clear()
    price_input.send_keys("186.00")
    browser.find_element_by_xpath("//button[@data-original-title='Save']").click()
    price_added = browser.find_element_by_xpath("//td[text()='Samsung Galaxy A50']/following-sibling::td[2]")
    assert price_added.text == "$186.00"
    print(price_added.text)


def test_deletion(browser, test_login):
    """Тест для функции удаления продукта"""
    browser.find_element_by_link_text("Catalog").click()
    ActionChains(browser).pause(0.5).perform()
    browser.find_element_by_link_text("Products").click()
    browser.find_element_by_xpath("//td[text()='Samsung Galaxy A50']/preceding-sibling::td/input").click()
    browser.find_element_by_xpath("//button[@data-original-title='Delete']").click()
    Alert(browser).accept()
    ActionChains(browser).pause(0.5).perform()
    product_deleted = browser.find_element_by_class_name("alert-success")
    assert product_deleted.text == "Success: You have modified products!\n×"
    print(product_deleted.text)
