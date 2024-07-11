from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


class TestStellarBurger:
    def test_exit_by_button_Log_Out(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON)).click()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.RECOVERY_BUTTON)).text == 'Восстановить пароль'
