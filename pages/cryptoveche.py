from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):
    select_role_btn = WebElement(id='auth_type_select')  # Select role for auth
    observer_btn = WebElement(css_selector='div[data-type="/observer_login"]')  # Observer locator
    username_field = WebElement(id='username')  # Username locator
    password_field = WebElement(id='password')  # Password locator
    submit_btn = WebElement(id='auth-btn')  # Submit auth form locator
    new_password_field = WebElement(id='new_password')  # New password field locator
    new_password_field2 = WebElement(id='repeat_new_password')  # Repeat new password field locator
    save_btn = WebElement(css_selector='div.profile-settings-block-save-button')  # Save new password locator
    add_poll = WebElement(id='main-btn')  # Add new poll button locator
    poll_title = WebElement(id='feTitle')  # Poll title locator
    voters = WebElement(id='is_voters_expandable')  # Expandable voters locator
    voters_open = WebElement(css_selector='div[data-type="open"]:nth-child(2)')  # Open voters locator
    add_question = WebElement(css_selector='div.add-question')  # Add new question locator
    question_type = WebElement(css_selector='div.selectBtn[data-type=""]')  # Choose question type locator
    question_by_choice = WebElement(css_selector='div[data-type="ynq"]')  # Question by choice type locator
    question_title = WebElement(css_selector='input.add-agenda-question-name-text-field')  # Question title locator
    add_event_button = WebElement(id='add_event')  # Add new poll button locator
