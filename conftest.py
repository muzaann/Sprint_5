import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import data
from locators import TestLocators
from data import TestUserData

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1280,800')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture()
def registration_and_authorization(driver):

    driver.find_element(*TestLocators.PERSONAL_AREA).click()
    driver.find_element(*TestLocators.REGISTRATION).click()
    driver.find_element(*TestLocators.REGISTRATION_NAME).send_keys(TestUserData.user['Имя'])
    driver.find_element(*TestLocators.REGISTRATION_EMAIL).send_keys(TestUserData.user['Email'])
    driver.find_element(*TestLocators.REGISTRATION_PASSWORD).send_keys(TestUserData.user['Пароль'])
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    driver.find_element(*TestLocators.PERSONAL_AREA).click()
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestUserData.user['Email'])
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestUserData.user['Пароль'])
    driver.find_element(*TestLocators.AUTH_BUTTON).click()
    WebDriverWait(driver, 3).until_not(expected_conditions.element_to_be_clickable((TestLocators.AUTH_BUTTON)))
