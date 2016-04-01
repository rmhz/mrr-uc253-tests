from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains

BROWSER = webdriver.Firefox()
URL = "mrr-uc253.appspot.com/unit2/signup"
URL_dev = "localhost:9999/unit2/signup"

##LOCATORS##

username_input_filed = 'input[name="username"]'
password_input_filed = 'input[name="password"]'
confpass_input_filed = 'input[name="verify"]'
email_input_filed = 'input[name="email"]'
submit_button = 'input[type="submit"]'

def enter_username(name):
	BROWSER.find_element_by_css_selector(username_input_filed).send_keys(name)

def enter_pass(passw):
	BROWSER.find_element_by_css_selector(password_input_filed).send_keys(passw)

def enter_confpass(passw):
	BROWSER.find_element_by_css_selector(confpass_input_filed).send_keys(passw)

def enter_email(email):
	BROWSER.find_element_by_css_selector(email_input_filed).send_keys(email)

def submit():
	BROWSER.find_element_by_css_selector(submit_button).click()

class TestSignUp():

	def setup_class(self):
		BROWSER.maximize_window()
		BROWSER.get(URL_dev)

	def teardown_class(self):
		#BROWSER.quit()
		pass

	def test_username(self):
		enter_username('testow')
		submit()
		time.sleep(3)
		errors = [el.get_attribute('textContent') for el in BROWSER.find_elements_by_css_selector('span[style="color:red"]')]
		assert 'Password is not valid' == errors[1]

#Test cases
#1 All fields empty
#2 Username, no password
#3 No username, password


