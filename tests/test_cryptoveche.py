# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -s tests/test_cryptoveche.py
#
import time
from pages.cryptoveche import MainPage

email = input('Please enter your email: ')
password = input('Please enter your password: ')
new_password = input('Please enter your new password: ')


def test_login_as_observer_and_change_password(browser):
    """ Login as observer, go to settings page and change password"""
    page = MainPage(browser, 'https://admin.evote74.dltc.spbu.ru/admin_auth')
    page.select_role_btn.click()  # Click select role button
    page.observer_btn.click()  # Choose observer button
    page.username_field = email  # Input email in the form field
    page.password_field = password  # Input password in the form field
    page.submit_btn.click()  # Click submit form button
    time.sleep(2)  # Wait until form will be submit
    # Open profile settings page
    page.get(f'https://admin.evote74.dltc.spbu.ru/users/{email}')
    browser.implicitly_wait(10)  # Wait until new_password_field will be acceptable
    page.new_password_field = new_password  # Input new password
    page.new_password_field2 = new_password  # Repeat new password
    page.save_btn.click()  # Click save button


def test_create_new_poll(browser):
    """ Login as admin and create new poll"""
    page = MainPage(browser, 'https://admin.evote74.dltc.spbu.ru/admin_auth')
    page.username_field = email  # Input email in the form field
    page.password_field = new_password  # Input password in the form field
    page.submit_btn.click()  # Click bubmit form button
    time.sleep(2)  # Wait until form will be submit
    page.get('https://admin.evote74.dltc.spbu.ru/main')  # Open main page
    browser.implicitly_wait(5)  # Wait until add_poll button will be displayed
    page.add_poll.click()  # Click add poll button
    page.poll_title = 'Test poll title'  # Input poll title
    page.voters.click()  # Choose poll voters type
    page.voters_open.click()  # Click open poll voters type
    page.add_question.click()  # Click add question button
    page.question_type.click()  # Choose question type
    page.question_by_choice.click()  # Click question by choice type button
    page.question_title = 'Test question title'  # Input question title
    page.add_event_button.click()  # Click submit new poll button
    time.sleep(2)  # Wait until form will be submit

