# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -s tests/test_cryptoveche.py
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#
import time

from pages.cryptoveche import LoginPage

email = input('Please enter your email: ')
password = input('Please enter your password: ')
new_password = input('Please enter your new password: ')


def test_login_as_observer_and_change_password(browser):
    page = LoginPage(browser, 'https://admin.evote74.dltc.spbu.ru/admin_auth')
    page.select_btn.click()
    page.observer_btn.click()
    page.username_field = email
    page.password_field = password
    page.submit_btn.click()
    time.sleep(2)
    page.get(f'https://admin.evote74.dltc.spbu.ru/users/{email}')
    browser.implicitly_wait(10)
    page.new_password_field = new_password
    page.new_password_field2 = new_password
    page.save_btn.click()
