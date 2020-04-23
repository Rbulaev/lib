#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

from selene.browser import open_url, element
from selene.support import by


import settings


class MainPage(object):
    login_button = "signInBtn"
    user_name_path = "//button[contains(@aria-owns, 'menu_container')]/span[@class='user-name']"
    search_field = 'searchBar'
    msg_after_search = "//span[@class='md-headline']"
    search_button = "//button[@aria-label='Отправить поиск']"
    advanced_search = "//span[text()='Расширенный поиск']"
    advanced_search_button = "//span[text()='Поиск']"
    material_type = "//span[text()='Расширенный поиск']"
    lang = "//span[text()='Расширенный поиск']"
    search_string = "textField"

    def open_test_page(self):
        open_url(settings.MAIN_URL)

    def click_login_button(self):
        element(by.id(MainPage.login_button)).click()
        return LoginPage()

    def see_user_name(self):
        return element(by.xpath(MainPage.user_name_path))

    def get_text_after_search(self):
        return element(by.xpath(MainPage.msg_after_search))

    def search_info(self, info):
        element(by.id(MainPage.search_field)).set(info)
        element(by.xpath(MainPage.search_button)).click()

    def open_advanced_search(self):
        element(by.xpath(MainPage.advanced_search)).click()

    def select_material_type(self, type_):
        element(by.xpath("//label[text()='Тип материала']/../md-select")).click()
        element(by.xpath("//md-option/div/span[text()='{}']".format(type_))).click()

    def select_lang(self, lang):
        element(by.xpath("//label[text()='Язык']/../md-select")).click()
        element(by.xpath("//md-content/md-option/div/span[text()='{}']".format(lang))).click()

    def publication_date(self, publication_date):
        element(by.xpath("//label[text()='Дата издания']/../md-select")).click()
        element(by.xpath("//md-option/div/span[text()='{}']".format(publication_date))).click()

    def write_advanced_text(self, advanced_text):
        element(by.name(MainPage.search_string)).set(advanced_text)

    def click_advanced_search_button(self):
        element(by.xpath(MainPage.advanced_search_button)).scroll_to().click()


class LoginPage(object):
    user_name = "//input[contains(@id, 'Username')]"
    user_password = "//input[contains(@id, 'Password')]"
    login_button = "//input[@value='Вход']"

    def write_user_name(self, user_name):
        element(by.xpath(LoginPage.user_name)).set(user_name)

    def write_password(self, password):
        element(by.xpath(LoginPage.user_password)).set(password)

    def press_enter_button(self):
        element(by.xpath(LoginPage.login_button)).click()
        return MainPage()

