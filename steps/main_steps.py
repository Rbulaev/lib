#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from behave import then, when, given
from selene.support.conditions import be

from pages.main_page import MainPage


@given('I open test page')
def open_test_page(context):
    context.page = MainPage()
    context.page.open_test_page()


@when('I click to the login button')
def click_login_button(context):
    context.page = context.page.click_login_button()


@then('I see user name:"{user_name}"')
def see_user_name(context, user_name):
    context.page.see_user_name().should(be.visible)
