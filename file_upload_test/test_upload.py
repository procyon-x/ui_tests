# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def test_upload(browser, test_login):
    """Тест для загрузки файла в админ-панели Opencart"""
    browser.find_element_by_link_text("Catalog").click()
    ActionChains(browser).pause(0.5).perform()
    browser.find_element_by_link_text("Downloads").click()
    browser.find_element_by_xpath("//a[@data-original-title='Add New']").click()
    upload_button = browser.find_element_by_id("button-upload")
    upload_button.click()
    file = browser.find_element_by_css_selector("input[type=file]")
    file.send_keys("D:\myfile.txt")
    ActionChains(browser).pause(1).perform()
    Alert(browser).accept()
    file_name = browser.find_element_by_css_selector("input[type=text]")
    file_name.send_keys("My File")
    browser.find_element_by_xpath("//button[@data-original-title='Save']").click()
