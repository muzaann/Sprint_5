
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestAuthorization:

    def test_login_main_page(self, driver):
        driver.find_element(*TestLocators.AUTH_BUTTON_MAIN).click()
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys('anna_muzafarova_5_123@yandex.ru')
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('Praktikum24')
        driver.find_element(*TestLocators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_personal_area(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys('anna_muzafarova_5_123@yandex.ru')
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('Praktikum24')
        driver.find_element(*TestLocators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_link_in_registration(self, driver):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.AUTH_LINK).click()
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys('anna_muzafarova_5_123@yandex.ru')
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('Praktikum24')
        driver.find_element(*TestLocators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_link_in_restore_password(self, driver):
        driver.find_element(*TestLocators.AUTH_BUTTON_MAIN).click()
        driver.find_element(*TestLocators.RESTORE_PASSWORD).click()
        driver.find_element(*TestLocators.AUTH_LINK).click()
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys('anna_muzafarova_5_123@yandex.ru')
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('Praktikum24')
        driver.find_element(*TestLocators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ORDER_BUTTON)))
        assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"
