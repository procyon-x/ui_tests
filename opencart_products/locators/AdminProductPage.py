# -*- coding: utf-8 -*-
"""Модуль с локаторами для страницы Products в админской панели"""


class AdminProductPage:
    add_new = "//a[@data-original-title='Add New']"
    meta_id = "input-meta-title1"
    save_button = "//button[@data-original-title='Save']"
    alert_class = "alert-success"
    edit_button = "//td[text()='Samsung Galaxy A50']/following-sibling::td[@class='text-right']/a"
    price_id = "input-price"
    price_cell = "//td[text()='Samsung Galaxy A50']/following-sibling::td[2]"
    product_checkbox = "//td[text()='Samsung Galaxy A50']/preceding-sibling::td/input"
    delete_button = "//button[@data-original-title='Delete']"
