#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from behave import when


@when('I write user name:"{user_name}"')
def write_user_name(context, user_name):
    context.page.write_user_name(user_name)


@when('I write user password:"{password}"')
def write_password(context, password):
    context.page.write_password(password)


@when('I press enter button')
def press_enter_button(context):
    context.page = context.page.press_enter_button()
