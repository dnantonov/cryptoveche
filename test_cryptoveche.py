import os
import time
from selenium import webdriver


chromedriver = os.path.abspath("chromedriver")
driver = webdriver.Chrome(executable_path=chromedriver)
usr = 'den88ant@yandex.ru'
psw = '1u1sb02839yD'

driver.get('https://admin.evote74.dltc.spbu.ru/admin_auth')
select_btn = driver.find_element_by_id('auth_type_select')
select_btn.click()

observer = driver.find_element_by_css_selector('div[data-type="/observer_login"]')
time.sleep(2)
observer.click()

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
username.send_keys(usr)
password.send_keys(psw)
submit_btn = driver.find_element_by_id('auth-btn')
submit_btn.click()
time.sleep(2)

driver.get(f'https://admin.evote74.dltc.spbu.ru/users/{usr}')
new_password = driver.find_element_by_id('new_password')
new_password2 = driver.find_element_by_id('repeat_new_password')
new_password.send_keys('05menima081993D')
new_password2.send_keys('05menima081993D')
save_btn = driver.find_element_by_css_selector('div.profile-settings-block-save-button')
save_btn.click()

driver.close()
