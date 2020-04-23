#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

from behave import then, when, given
from selene.support.conditions import be, have

from pages.pages import MainPage


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


@when('I search info:"{date_}"')
def see_user_name(context, date_):
    context.page.search_info(date_)


@then('I see message:"{msg}"')
def see_user_name(context, msg):
    context.page.get_text_after_search().should(have.text(msg))


@when('I open advanced search')
def see_user_name(context):
    context.page.open_advanced_search()


@when('I select material type:"{type_}"')
def see_user_name(context, type_):
    context.page.select_material_type(type_)


@when('I select lang:"{select_lang}"')
def see_user_name(context, select_lang):
    context.page.select_lang(select_lang)


@when('I select publication date:"{publication_date}"')
def see_user_name(context, publication_date):
    context.page.publication_date(publication_date)


@when('I write advanced text"{advanced_text}"')
def see_user_name(context, advanced_text):
    context.page.write_advanced_text(advanced_text)


@when('I click advanced search button')
def see_user_name(context):
    context.page.click_advanced_search_button()
