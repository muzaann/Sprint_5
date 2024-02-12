
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestSections:

    def test_transition_to_sauces_succses(self, driver):
        driver.find_element(*TestLocators.SAUCES_SECTION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.SPICY_SAUCE)))
        assert driver.find_element(*TestLocators.SPICY_SAUCE).text == 'Соус Spicy-X'

    def test_transition_to_stuffing_succses(self, driver):
        driver.find_element(*TestLocators.STUFFING_SECTION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BEEF_METEORITE)))
        assert driver.find_element(*TestLocators.BEEF_METEORITE).text == 'Говяжий метеорит (отбивная)'

    def test_transition_to_buns_succses(self, driver):
        driver.find_element(*TestLocators.STUFFING_SECTION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BEEF_METEORITE)))
        driver.find_element(*TestLocators.BUNS_SECTION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.FLUORESCENT_BUN)))
        assert driver.find_element(*TestLocators.FLUORESCENT_BUN).text == 'Флюоресцентная булка R2-D3'
