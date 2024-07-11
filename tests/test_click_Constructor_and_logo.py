from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from constants import Constants
from locators import Locators


class TestStellarBurger:

    def test_click_Constructor(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.COLLECT_BURGER_BUTTON))
        assert driver.find_element(*Locators.COLLECT_BURGER_BUTTON).text == 'Соберите бургер'

    def test_click_logo(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.COLLECT_BURGER_BUTTON))
        assert driver.find_element(*Locators.COLLECT_BURGER_BUTTON).text == 'Соберите бургер'