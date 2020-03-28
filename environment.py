# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from selene import config, browser
from selene.browsers import BrowserName
from selenium import webdriver

import settings


def before_all(context):
    config.browser_name = BrowserName.CHROME
    # скрины
    config.reports_folder = "./reports"


def before_scenario(context, scenario):
    set_default_driver()


def set_default_driver():
    # настройки хрома
    options = webdriver.ChromeOptions()
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')

    # по умолчанию 4, можно настроить:)
    # config.timeout = 666

    # для удаленного
    if settings.SELENIUM_SERVER_STANDALONE:
        driver = webdriver.Remote(
            command_executor=settings.SELENIUM_SERVER_STANDALONE,
            desired_capabilities=options.to_capabilities()
        )
        browser.set_driver(driver)
