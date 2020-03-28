#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from selene.browser import open_url, element
from selene.support import by


import settings


class MainPage(object):
    login_button = "signInBtn"
    user_name_path = "//button[contains(@aria-owns, 'menu_container')]/span[@class='user-name']"

    def open_test_page(self):
        open_url(settings.MAIN_URL)

    def click_login_button(self):
        element(by.id(MainPage.login_button)).click()
        return LoginPage()

    def see_user_name(self):
        return element(by.xpath(MainPage.user_name_path))


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
