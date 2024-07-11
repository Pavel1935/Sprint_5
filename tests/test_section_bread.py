from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators

class TestStellarBurger:
    def test_registration(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.SAUCE_BUTTON)).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(Locators.BREAD_BUTTON)).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.FLUR_BULKA)).text == 'Флюоресцентная булка R2-D3'