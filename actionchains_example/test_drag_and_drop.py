# -*- coding: utf-8 -*-
"""Пример работы с ActionChains"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def test_drag_and_drop():
    """Тест с drag&drop, складывающий документы в корзину"""
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("https://marcojakob.github.io/dart-dnd/basic/")
    document = browser.find_elements_by_css_selector("div[class='container'] img")
    trash = browser.find_element_by_class_name("trash")
    for doc in document:
        ActionChains(browser).pause(0.5).move_to_element(doc).click_and_hold().move_to_element(
            trash).release().perform()

    browser.quit()
