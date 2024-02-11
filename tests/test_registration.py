
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
import random


class TestRegistration:

    def test_registration_successfully(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.REGISTRATION_NAME).send_keys("Музафарова Анна")
        driver.find_element(*TestLocators.REGISTRATION_EMAIL).send_keys(f'anna_muzafarova_5_{random.randint(100, 999)}@yandex.ru')
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD).send_keys('Praktikum24')
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.AUTH_BUTTON)))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()

    def test_registration_unvalid_password_false(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.REGISTRATION_NAME).send_keys("Музафарова Анна")
        driver.find_element(*TestLocators.REGISTRATION_EMAIL).send_keys('anna_muzafarova_5_146@yandex.ru')
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD).send_keys('1234')
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.UNVALID_PASSWORD)))
        assert driver.find_element(*TestLocators.UNVALID_PASSWORD).text == "Некорректный пароль"
        driver.quit()