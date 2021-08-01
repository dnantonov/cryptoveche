import os

from pages.base import WebPage
from pages.elements import WebElement


class LoginPage(WebPage):

    # email = input('Please enter your email: ')
    # password = input('Please enter your password: ')
    # new_password = input('Please enter your new password: ')

    select_btn = WebElement(id='auth_type_select')
    observer_btn = WebElement(css_selector='div[data-type="/observer_login"]')
    username_field = WebElement(id='username')
    password_field = WebElement(id='password')
    submit_btn = WebElement(id='auth-btn')
    new_password_field = WebElement(id='new_password')
    new_password_field2 = WebElement(id='repeat_new_password')
    save_btn = WebElement(css_selector='div.profile-settings-block-save-button')

