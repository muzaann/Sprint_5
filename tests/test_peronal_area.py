
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestPersonalArea:

    def test_transition_to_personal_area_succses(self, driver, registration_and_authorization):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ACCOUNT)))
        assert driver.find_element(*TestLocators.ACCOUNT).text == 'Профиль'
        driver.quit()

    def test_transition_to_constructor_succses(self, driver, registration_and_authorization):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ACCOUNT)))
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((TestLocators.ASSEMBLE_A_BURGER)))
        assert driver.find_element(*TestLocators.ASSEMBLE_A_BURGER).text == 'Соберите бургер'
        driver.quit()

    def test_transition_to_logo_succses(self, driver, registration_and_authorization):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ACCOUNT)))
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((TestLocators.ASSEMBLE_A_BURGER)))
        assert driver.find_element(*TestLocators.ASSEMBLE_A_BURGER).text == 'Соберите бургер'
        driver.quit()

    def test_quit_personal_area_succses(self, driver, registration_and_authorization):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.ACCOUNT)))
        driver.find_element(*TestLocators.ACCOUNT_EXIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.AUTH_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()